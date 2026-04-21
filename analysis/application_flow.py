"""Application flow dashboard.

Reads data/applications.yaml and renders an interactive Sankey diagram showing
how applications have moved through stages (applied -> screen -> interview ...)
plus a summary bar of current status counts. Clicking any node or link in the
Sankey reveals the specific applications in a detail panel below.

Usage:
    python analysis/application_flow.py

Outputs analysis/application_flow.html
"""

import argparse
import json
from collections import Counter
from pathlib import Path

import plotly.graph_objects as go
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "applications.yaml"
OUT = Path(__file__).parent / "application_flow.html"
OUT_PUBLIC = Path(__file__).parent / "example_application_flow.html"

STAGE_ORDER = [
    "applied",
    "reapplied",
    "screen",
    "technical_screen",
    "hiring_manager_screen",
    "assessments",
    "onsite",
    "offer",
    "accepted",
    "rejected",
    "declined",
    "withdrawn",
    "ghosted",
]

STAGE_LABEL = {
    "applied": "Applied",
    "reapplied": "Reapplied",
    "screen": "Screen",
    "technical_screen": "Technical Screen",
    "hiring_manager_screen": "Hiring Manager Screen",
    "assessments": "Assessments",
    "onsite": "Onsite",
    "offer": "Offer",
    "accepted": "Accepted",
    "rejected": "Rejected",
    "declined": "Declined",
    "withdrawn": "Withdrawn",
    "ghosted": "Ghosted",
}

STAGE_COLOR = {
    "applied": "#94a3b8",
    "reapplied": "#64748b",
    "screen": "#3b82f6",
    "technical_screen": "#6366f1",
    "hiring_manager_screen": "#8b5cf6",
    "assessments": "#a855f7",
    "onsite": "#ec4899",
    "offer": "#10b981",
    "accepted": "#059669",
    "rejected": "#ef4444",
    "declined": "#f97316",
    "withdrawn": "#f59e0b",
    "ghosted": "#78716c",
}

TERMINAL_NEGATIVE = {"rejected", "declined", "withdrawn", "ghosted", "accepted"}


def hex_to_rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def load_apps():
    with DATA.open() as f:
        return yaml.safe_load(f)["applications"]


def app_summary(a):
    return {
        "company": a["company"],
        "role": a["role"],
        "status": a["status"],
        "date_applied": a.get("date_applied", ""),
        "source": a.get("source", ""),
    }


def build_sankey(apps):
    """Build Sankey + mappings from node/link index to list of applications.

    Node = a stage (e.g., "Applied", "Rejected", "Still at Screen").
    Link = a transition between stages, or a "still at stage" flow.

    Returns (fig, node_apps, link_apps, current_at).
    node_apps[node_idx] = list of app dicts that EVER touched that stage
    link_apps[link_idx] = list of app dicts that made that specific transition
    """
    transitions = Counter()
    transition_apps = {}  # (src, tgt) -> list of app dicts
    for a in apps:
        hist = a.get("status_history", [])
        for i in range(len(hist) - 1):
            key = (hist[i]["status"], hist[i + 1]["status"])
            transitions[key] += 1
            transition_apps.setdefault(key, []).append(app_summary(a))

    # Apps currently at each stage (last history entry)
    current_at = Counter()
    current_apps = {}
    for a in apps:
        hist = a.get("status_history", [])
        if hist:
            cur = hist[-1]["status"]
            current_at[cur] += 1
            current_apps.setdefault(cur, []).append(app_summary(a))

    # Apps that EVER touched each stage
    stage_apps = {}
    for a in apps:
        hist = a.get("status_history", [])
        touched = {h["status"] for h in hist}
        for s in touched:
            stage_apps.setdefault(s, []).append(app_summary(a))

    # Stages present in the data
    present = set(transitions) if False else set()
    for s, t in transitions:
        present.add(s)
        present.add(t)
    present.update(current_at.keys())

    entry_nodes = [s for s in STAGE_ORDER if s in present]
    still_at_stages = [s for s in entry_nodes if s not in TERMINAL_NEGATIVE]

    labels, colors = [], []
    node_idx = {}
    node_apps = {}  # idx -> list of app dicts

    for s in entry_nodes:
        idx = len(labels)
        node_idx[("stage", s)] = idx
        # Label shows count touching this stage
        total_through = len(stage_apps.get(s, []))
        labels.append(f"{STAGE_LABEL.get(s, s)} ({total_through})")
        colors.append(STAGE_COLOR.get(s, "#888888"))
        node_apps[idx] = stage_apps.get(s, [])

    for s in still_at_stages:
        n = current_at.get(s, 0)
        if n == 0:
            continue
        idx = len(labels)
        node_idx[("still", s)] = idx
        labels.append(f"Still at {STAGE_LABEL.get(s, s)} ({n})")
        colors.append(hex_to_rgba(STAGE_COLOR.get(s, "#888888"), 0.4))
        node_apps[idx] = current_apps.get(s, [])

    src, tgt, val, link_colors = [], [], [], []
    link_apps = {}  # link idx -> list of app dicts

    for (s, t), v in transitions.items():
        if ("stage", s) not in node_idx or ("stage", t) not in node_idx:
            continue
        link_idx = len(src)
        src.append(node_idx[("stage", s)])
        tgt.append(node_idx[("stage", t)])
        val.append(v)
        link_colors.append(hex_to_rgba(STAGE_COLOR.get(t, "#888888"), 0.33))
        link_apps[link_idx] = transition_apps.get((s, t), [])

    for s in still_at_stages:
        n = current_at.get(s, 0)
        if n == 0 or ("still", s) not in node_idx:
            continue
        link_idx = len(src)
        src.append(node_idx[("stage", s)])
        tgt.append(node_idx[("still", s)])
        val.append(n)
        link_colors.append(hex_to_rgba(STAGE_COLOR.get(s, "#888888"), 0.2))
        link_apps[link_idx] = current_apps.get(s, [])

    # Build human-readable labels for nodes/links (for detail panel headings)
    node_titles = list(labels)
    link_titles = []
    for i, (s_idx, t_idx) in enumerate(zip(src, tgt)):
        s_label = labels[s_idx].split(" (")[0]
        t_label = labels[t_idx].split(" (")[0]
        link_titles.append(f"{s_label} → {t_label}")

    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                pad=20,
                thickness=22,
                line=dict(color="rgba(0,0,0,0.1)", width=0.5),
                label=labels,
                color=colors,
            ),
            link=dict(source=src, target=tgt, value=val, color=link_colors),
        )
    )
    return fig, node_apps, link_apps, node_titles, link_titles, current_at


def build_summary_bar(current_at):
    ordered = [(s, current_at[s]) for s in STAGE_ORDER if current_at.get(s, 0) > 0]
    labels = [STAGE_LABEL[s] for s, _ in ordered]
    counts = [c for _, c in ordered]
    colors = [STAGE_COLOR[s] for s, _ in ordered]

    fig = go.Figure(
        go.Bar(
            x=labels,
            y=counts,
            marker_color=colors,
            text=counts,
            textposition="outside",
            hovertemplate="%{x}: %{y}<extra></extra>",
        )
    )
    fig.update_layout(
        yaxis_title="Applications",
        xaxis_title="",
        showlegend=False,
        margin=dict(l=40, r=20, t=30, b=40),
    )
    return fig


def main(public=False):
    apps = load_apps()
    sankey, node_apps, link_apps, node_titles, link_titles, current_at = build_sankey(
        apps
    )
    bar = build_summary_bar(current_at)

    title_suffix = "" if public else " (click any node or link)"
    sankey.update_layout(
        title=dict(
            text=f"Application Flow — {len(apps)} total applications{title_suffix}",
            x=0.5,
            xanchor="center",
            font=dict(size=18),
        ),
        font=dict(size=12),
        height=620,
        margin=dict(l=20, r=20, t=60, b=20),
    )

    bar.update_layout(
        title=dict(
            text="Current Status", x=0.5, xanchor="center", font=dict(size=18)
        ),
        height=360,
    )

    sankey_div_id = "sankey-figure"
    sankey_html = sankey.to_html(
        include_plotlyjs="cdn", full_html=False, div_id=sankey_div_id
    )
    bar_html = bar.to_html(include_plotlyjs=False, full_html=False)

    # JSON data for click handlers (private only — contains company/role names)
    click_data = {
        "nodeApps": {str(k): v for k, v in node_apps.items()},
        "linkApps": {str(k): v for k, v in link_apps.items()},
        "nodeTitles": node_titles,
        "linkTitles": link_titles,
    }

    js = f"""
<script>
const CLICK_DATA = {json.dumps(click_data)};
const sankeyDiv = document.getElementById('{sankey_div_id}');
const detailPanel = document.getElementById('detail-panel');
const detailHeading = document.getElementById('detail-heading');
const detailList = document.getElementById('detail-list');

function renderApps(title, apps) {{
    detailHeading.textContent = title + ' (' + apps.length + ')';
    if (apps.length === 0) {{
        detailList.innerHTML = '<p style="color:#888;">No applications in this segment.</p>';
        return;
    }}
    let html = '<table class="apps-table"><thead><tr>' +
        '<th>Company</th><th>Role</th><th>Current Status</th><th>Applied</th><th>Source</th>' +
        '</tr></thead><tbody>';
    for (const a of apps) {{
        const src = a.source
            ? '<a href="' + a.source + '" target="_blank" rel="noopener">link</a>'
            : '';
        html += '<tr>' +
            '<td>' + a.company + '</td>' +
            '<td>' + a.role + '</td>' +
            '<td class="status-' + a.status + '">' + a.status + '</td>' +
            '<td>' + a.date_applied + '</td>' +
            '<td>' + src + '</td>' +
            '</tr>';
    }}
    html += '</tbody></table>';
    detailList.innerHTML = html;
    detailPanel.scrollIntoView({{behavior: 'smooth', block: 'nearest'}});
}}

sankeyDiv.on('plotly_click', function(e) {{
    const pt = e.points[0];
    // Link clicks have .source and .target as objects; node clicks don't
    const isLink = pt.source !== undefined && typeof pt.source === 'object';
    if (isLink) {{
        const linkIdx = pt.pointNumber;
        renderApps(
            CLICK_DATA.linkTitles[linkIdx] || 'Link',
            CLICK_DATA.linkApps[String(linkIdx)] || []
        );
    }} else {{
        const idx = pt.index !== undefined ? pt.index : pt.pointNumber;
        renderApps(
            CLICK_DATA.nodeTitles[idx] || 'Node',
            CLICK_DATA.nodeApps[String(idx)] || []
        );
    }}
}});
</script>
"""

    # Detail panel + click-handler JS only in private mode — the JSON blob
    # contains raw company/role names we don't want on a public page.
    detail_panel_html = "" if public else f"""
<div id='detail-panel'>
  <h3 id='detail-heading'>Click a node or link above to see applications</h3>
  <div id='detail-list'>
    <p class='hint'>For example: click "Applied" to see every application, or
       "Applied → Rejected" to see the apps that ended there.</p>
  </div>
</div>"""
    script_block = "" if public else js
    subtitle_suffix = (
        "" if public else " · click any segment of the Sankey to see detail"
    )
    public_notice = (
        "<div class='sub' style='color:#888;font-style:italic;margin-top:4px;'>"
        "Public view — aggregate counts only. Run without --public locally to "
        "get the interactive detail panel.</div>"
        if public else ""
    )

    html = f"""<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<title>Application Flow Dashboard</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif;
         margin: 20px; background: #fafafa; color: #1a1a1a; }}
  h1 {{ text-align: center; margin: 8px 0 4px; font-weight: 600; }}
  .sub {{ text-align: center; color: #666; margin-bottom: 16px; }}
  #detail-panel {{ background: white; border-radius: 8px; padding: 20px;
                  margin-top: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
  #detail-heading {{ margin: 0 0 12px; font-size: 18px; font-weight: 600; }}
  #detail-list {{ max-height: 500px; overflow-y: auto; }}
  .apps-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .apps-table th, .apps-table td {{ text-align: left; padding: 6px 10px;
                                    border-bottom: 1px solid #eee; vertical-align: top; }}
  .apps-table th {{ background: #f5f5f5; font-weight: 600; }}
  .apps-table tr:hover {{ background: #fafafa; }}
  .status-applied {{ color: #64748b; }}
  .status-screen {{ color: #3b82f6; font-weight: 600; }}
  .status-technical_screen {{ color: #6366f1; font-weight: 600; }}
  .status-hiring_manager_screen {{ color: #8b5cf6; font-weight: 600; }}
  .status-assessments {{ color: #a855f7; font-weight: 600; }}
  .status-onsite {{ color: #ec4899; font-weight: 600; }}
  .status-offer, .status-accepted {{ color: #059669; font-weight: 600; }}
  .status-rejected {{ color: #ef4444; }}
  .status-declined, .status-withdrawn {{ color: #f97316; }}
  .hint {{ color: #888; font-size: 13px; margin: 0; }}
</style>
</head>
<body>
<h1>Resume Builder — Application Flow</h1>
<div class='sub'>{len(apps)} applications tracked{subtitle_suffix}</div>
{public_notice}
{sankey_html}
{detail_panel_html}
{bar_html}
{script_block}
</body>
</html>
"""
    out = OUT_PUBLIC if public else OUT
    out.write_text(html)
    print(f"Wrote {out}")
    print(f"\nCurrent status breakdown:")
    for s in STAGE_ORDER:
        if current_at.get(s, 0) > 0:
            print(f"  {STAGE_LABEL[s]:<30} {current_at[s]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--public",
        action="store_true",
        help="Generate a public-safe version (counts only, no per-app detail).",
    )
    args = parser.parse_args()
    main(public=args.public)
