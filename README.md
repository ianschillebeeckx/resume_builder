# Resume Builder

An AI-native system for generating tailored LaTeX resumes from a master CV database. Built entirely through conversational collaboration with [Claude Code](https://claude.ai/code).

## Goals

1. **Create an AI-native workflow for generating a custom resume for each JD.** Every job posting gets a tailored resume — not a generic template swap, but a ground-up reframing of experience, terminology, and title calibration matched to the specific role.
2. **Track the progress of applications and interviews.** Maintain a structured log of every application, status change, and interview stage — making the job search itself a data-driven process.
3. **Practice modern AI tooling.** This project is a hands-on exercise in [Claude Code](https://claude.ai/code) (CLI), Claude Code skills (custom commands), and [Claude Cowork](https://claude.ai/cowork) (browser-based application submission).

## Vision

The resume/JD application process is fundamentally an autoencoder type communication protocol that causes inefficiencies. On one side, the applicant's full context — their CV, career trajectory, and life's work — gets compressed into a 1-2 page resume. On the other side, the company's full context — culture, org structure, reporting lines, team dynamics, actual job requirements — gets compressed into a 1-page JD. Both sides lose information in the compression, and that information loss drives the inefficiencies of the entire hiring pipeline:

- Recruiter screens that re-ask what's already on the resume
- Hiring manager interviews that probe for context the JD never provided
- Mismatches that don't surface until onsite
- Generic resumes that cram broad information to cover multiple possible roles, diluting the signal for any specific one
- Applicants who must apply to dozens of roles because they can't fully evaluate fit from a compressed JD — taking many shots on goal to compensate for the information loss

In the near future, I expect agents to make this process dramatically more efficient by exposing the full, uncompressed context on both sides — allowing candidate and company agents to negotiate fit at a depth that compressed documents never could.

This project is the intermediate step: using AI to make the compression as lossless as possible, generating resumes that are maximally tailored to the signal in each JD rather than settling for a generic one-size-fits-all document.

## How It Works

The system operates in two phases:

**Phase 1: Build the CV Database.** Parse existing resumes into a comprehensive master CV (`data/cv.yaml`). This is the verbose, complete record of all experience — different resumes may describe the same role with different focus areas (technical vs leadership), and all perspectives are preserved additively.

**Phase 2: Generate Tailored Resumes.** Given a job posting and the CV database, generate a tailored 2-page LaTeX resume. The generation process:

1. Analyzes job requirements, keywords, and seniority level
2. Selects relevant experience entries from the CV database
3. Chooses bullets that best match the role (technical, leadership, IC, etc.)
4. Adapts terminology to mirror job posting language
5. Calibrates titles to match target level (VP for VP roles, Director for Director roles, etc.)
6. Outputs LaTeX using the template, compiles to PDF

Each resume is a conversation — the initial generation is followed by iterative critique, verb corrections ("directed" vs "built"), domain reframing, and structural adjustments until the resume is sharp.

## The AI-Native Workflow

This entire system — the CV database, every resume, every cover letter, the application tracker, even this README — was built through Claude Code. The workflow looks like:

```
"new resume: [linkedin URL]"     → fetches JD, saves it, builds tailored resume
"mark applied"                   → logs to application tracker
"critique this resume"           → honest gap analysis with specific fixes
"mark [company] rejected"        → updates status tracking
"commit"                         → stages and commits everything
```

A typical session produces 10-15 tailored resumes in a few hours, each with JD-specific framing, title calibration, and iterative refinement.

## Skills (Claude Code Commands)

The system is driven by custom skills in `.claude/commands/`:

| Skill | Description |
|-------|-------------|
| `/cv-build` | Parse existing resumes into the master CV database |
| `/cv-add` | Add new experience or skill entries to the database |
| `/job-save` | Fetch a job posting from a URL and save locally |
| `/resume-generate` | Generate a tailored LaTeX resume from CV + job posting |
| `/resume-critique` | Honest critique identifying gaps, strengths, and domain fit |
| `/job-apply` | Fill out ATS application forms (requires Claude Cowork) |

## Directory Structure

```
.claude/commands/       # Claude Code skills
data/cv.yaml            # Master CV database (YAML)
templates/              # LaTeX resume template
input/jobs/             # Job descriptions (examples included)
output/                 # Generated resumes and cover letters (examples included)
```

## Examples

The repo includes anonymized examples showing the full pipeline:

| Example | What it demonstrates |
|---------|---------------------|
| `example-sr-manager-data-science-growth` | Leadership role with revenue + growth dual mandate |
| `example-senior-data-scientist` | IC role with manager-to-IC mission statement |
| `example-director-analytics-experimentation` | Leadership role with cover letter |
| `example-sr-director-data-science-health` | Healthcare domain tailoring |

Each example includes a paired JD (`input/jobs/`) and generated resume (`output/`), showing how the same CV database produces different resumes for different roles.

> **Note:** Real application data (specific companies, JDs, and tailored resumes) is gitignored. The examples are anonymized versions of real outputs.

## Design Decisions

- **Additive CV merging** — different resumes may emphasize different aspects of the same role. All bullet variations are preserved; the generation skill selects appropriate ones later.
- **Title calibration** — molecular diagnostics is a small field with small organizations, so titles tend to be inflated relative to how larger companies scope similar roles and responsibilities. Titles are calibrated at the presentation layer to better match how the target organization would title equivalent scope (e.g., VP becomes Sr. Director for Director-level roles, Director for Manager-level roles). The CV database always stores actual titles.
- **Terminology adaptation** — the CV uses precise language (e.g., "Revenue Cycle Management"). Resumes adapt terminology to mirror job posting language (e.g., "payment workflows" for fintech roles).
- **2-page default** — senior roles need space. The system defaults to 2 pages rather than artificially compressing to 1.

## Application Tracking

The system maintains a YAML-based application tracker (`data/applications.yaml`, gitignored) that logs:
- Company, role, source URL, date applied
- Resume and additional materials used
- Status history (applied → screen → interview → offer/rejected)
- Notes on comp, location, title calibration, and role-specific context

Status updates are conversational: "mark [company] rejected" or "mark [company] screen."

## Tech Stack

- **Claude Code** (Opus) — all generation, critique, and workflow orchestration
- **LaTeX** (`pdflatex`) — resume compilation
- **YAML** — CV database and application tracking
- **Git** — version control with structured commits

## Getting Started

1. Clone the repo
2. Install LaTeX (`pdflatex`) — e.g., `brew install --cask mactex` on macOS
3. Open with Claude Code: `claude` in the repo directory
4. Build your CV: `/cv-build` with your existing resumes in `input/resumes/`
5. Generate a resume: paste a job URL and say "new resume"

## License

This project is open source for reference and inspiration. The system design, skills, and workflow patterns are freely reusable. The CV data represents one person's career and is not intended for reuse.
