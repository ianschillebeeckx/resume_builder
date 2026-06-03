# Resume Generate

Generate a tailored LaTeX resume for a specific job posting.

## Arguments

$ARGUMENTS - (optional) Name of job file in `input/jobs/`, or leave blank to select

## Instructions

### 1. Setup
- If no job specified, list available jobs in `input/jobs/` and ask which one
- Read the job posting file
- Read the master CV database from `data/cv.yaml`
- Use `templates/ian-template.tex` as base (has contact info and education pre-filled)

### 2. Analyze Job Requirements
- Identify core requirements (technical skills, leadership, domain expertise)
- Map requirements to CV experiences and achievements
- Note key keywords and terminology from job description

### 3. Strategic Positioning
- **Experience selection**: Choose 3-4 most relevant roles
- **Bullet allocation**: More recent/relevant roles get more bullets (4-6), older roles get fewer (2-4)
- **Balance**: Mix direct job matches with excellence indicators (awards, publications, exceptional outcomes)
- **Terminology**: Generalize domain-specific terms to broader applicability where appropriate
  - Example: "clinical validation study" → "prespecified randomized multi-center study"
  - Example: "biomarker" → "production ML model"
  - Example: "product volume" → "unit volume" (more universal)
  - Example: "historically controlled" → "pre-post controlled analysis" (less clinical)
- **Role consolidation**: When combining multiple titles at one company, use "Head of [Function]" rather than final title if progression was gradual

### 4. Content Selection Guidelines
- Lead with strongest matches to job requirements
- Emphasize quantified business impact (%, $, time, scale)
- Include cross-functional collaboration and team leadership
- Highlight 0→1 platform/product building where relevant
- Show technical depth through specific methods/tools
- **Platform story**: Show reusable systems, not just one-off models (dashboards, tools others use)
- **Model monitoring**: Include automated revalidation, drift detection, maintenance examples
- **Modern methods**: Include current approaches (Prophet, TFT) alongside classics (ARIMA, LSTM)
- **Bridge domain gaps**: Include universal business metrics (churn, revenue) alongside domain-specific work

### 5. Generate LaTeX Resume
- Use ian-template.tex structure
- Fill Experience section with selected roles and tailored bullets
- Create Technical Skills section with categories ordered by relevance to job
- Include Publications section if research/technical depth is valued
- **Target**: 1 page (adjust bullets if needed to fit)

### 6. Output
- Write to `output/[company]-[role-slug].tex`
- Compile to PDF
- **Target 1 page**: Default margins are 0.5in; can reduce to 0.4in if needed for space
- Provide summary of:
  - What was emphasized
  - Key positioning choices
  - Suggested adjustments if needed

### 7. Post-Generation Review
After generating, suggest running `/resume-critique` to analyze from hiring manager's perspective.

## Role-Type Templates

For similar roles, start from an existing tailored resume rather than from scratch:

| Role Type | Template | Key Features |
|-----------|----------|--------------|
| DS/Analytics Leadership (default) | `output/zoox-director-bi-enterprise-analytics.tex` | BI portfolio (Tableau), GenAI section, forecasting, churn, causal inference, OKRs/KPIs, model governance, ML infrastructure, 6 Cofactor bullets, cross-functional (CEO/CFO/COO), Board participation |
| Healthcare DS Leadership | `output/medix-sr-director-data-science-analytics.tex` | Healthcare framing throughout, RCM/claims, provider network analytics, regulatory compliance (CAP/CLIA), same core bullets with healthcare terminology |
| Tech/SaaS DS Leadership | `output/highlevel-sr-director-data-science.tex` | De-healthcare'd language, experimentation/A/B testing framing, product analytics, GenAI prominent, ML model registries/feature stores, SaaS metrics (churn, revenue forecasting) |
| GTM / BizOps / Product DS Manager (tech) | `output/google-business-data-science-manager-gbso.tex` | **Gold standard for tech BizOps roles.** Player/coach mission with $$ + earnings-call anchor; X/Y/Z bullet structure per Google guidance; verb discipline visible ("built initial myself + directed team to scale"); GTM terminology (not Commercial); causal inference + incrementality + propensity stacked in skills; BERT sentiment bullet bridges customer-sentiment JD pillars; quarterly drift detection + revalidation signals production-ML maturity; "personally built ProductLLM/NBA + oversaw contractor RAG build" distinguishes IC vs delegated work; RCM jargon contextualized ("bill-request information sent to insurers") |
| Growth / Revenue DS Manager (tech) | `output/checkr-sr-manager-data-ml-revenue-growth.tex` | Tech-revenue framing without earnings-call anchor; Revenue & Unit Economics + Growth & Experimentation skills rows; PLG / activation / conversion / funnel framing; LTV/pricing/packaging language; AI-first operations; Wall Street reporting in forecasting bullet; suited to Stripe/Mercury/Gusto/Snowflake-style Sr Manager roles |
| Product Science IC (tech) | `output/tiktok-data-science-lead-quant-modeling.tex` | **IC pivot canonical.** Title calibrated to **Director** (not VP, not Principal); summary leads with "hands-on product data scientist... I build the model myself"; **5 spine bullets** designed for swap-and-reuse across Product Sci IC roles: (1) forecasting personal build (ARIMA/Prophet, 6%→0.9%), (2) propensity/retention $270M (LTV-adjacent bridge via changepoint+DP), (3) causal+A/B $25M (prespecified z-test), (4) personally-built ProductLLM + prototyped NBA, (5) AI-native Codex stack (IC-throughput compounding); team-management bullet demoted to last; PhD line has NO parenthetical; bullets 5–6 are tunable per JD (quasi-experimental DiD/ITS/RDD/IV or metric-layer framing). Used for Moloco (ad-tech/incrementality tweak), Whatnot (marketplace tweak), Microsoft Copilot (LLM-product foreground). |
| Applied Research / Computational Scientist IC (tech) | `output/meta-data-scientist-products-applied-research.tex` | **IC canonical for research-flavored Product DS roles** (Meta Applied Research, FAIR-adjacent, methodology-novelty teams). Same IC framing as Product Science canonical (Director title, build verbs, demoted team-mgmt) but **summary leads with builder-first identity** ("personally build the first models, the first prototypes, and the first tools") and **Nature + 3 patents + PhD-fastest** promoted high for Applied Research credibility; CareDx bullets reordered: ProductLLM personally-built and NBA personally-prototyped lead, then forecasting personally-built initial, then causal designed-and-led, then Codex stack built-custom, then propensity designed; Cofactor leads with Nature + 3 patents bullet, then "Built 2 production ML models end-to-end"; Predictive Modeling & ML leads skills, then Causal Inference, then dedicated Research & Communication row. |

When using a template:
1. Copy to new output file
2. Adjust bullets for specific JD emphasis
3. Swap/add relevant projects from CV
4. Update technical skills ordering

## Selection Criteria Examples

**For forecasting/data science leadership roles:**
- Forecasting transformation metrics (error reduction, multiple horizons like 3/6/12/24 months)
- Forecasting operationalization (dashboards, automated revalidation, stakeholder access)
- Team size, budget, cross-functional partnerships (CEO/CFO/COO level)
- Causal inference, predictive modeling, churn prediction
- Production ML systems with monitoring
- Executive communication and planning integration

**For ML/AI platform roles:**
- 0→1 platform building
- Production ML infrastructure
- Model monitoring and explainability
- Cloud optimization metrics
- Research publications/patents

**For product/technical leadership:**
- Roadmapping, OKRs
- Regulatory/validation expertise
- Multi-stakeholder coordination
- Revenue/business impact

## Notes

- Abbreviate titles: "Vice President" → "VP"
- **Title calibration**: When the target role is Director-level (i.e. below VP), downgrade CareDx titles from "VP" to "Sr. Director". This is a presentation-layer adjustment — do not modify the CV database.
- Match keywords from job description where authentic
- More recent work deserves more detail
- Excellence indicators: fastest PhD, Nature paper (2nd most downloaded), Board participation, etc.
- Ask if anything seems missing or should be adjusted
- **CV sync**: When refining resume bullets, propagate significant additions/changes back to `data/cv.yaml`
- **LaTeX tips**: Use `$\sim$` for tilde (~), `\parbox[t]{3.5in}{...}` for multi-line entries in tables
