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
| Tech/SaaS DS Leadership | `output/openai-head-of-data-science-forecasting.tex` | Unit volume forecasting, churn prediction, Streamlit dashboards, automated revalidation, cross-functional (CEO/CFO/COO), causal inference, modern methods (Prophet) |

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
- Match keywords from job description where authentic
- More recent work deserves more detail
- Excellence indicators: fastest PhD, Nature paper (2nd most downloaded), Board participation, etc.
- Ask if anything seems missing or should be adjusted
- **CV sync**: When refining resume bullets, propagate significant additions/changes back to `data/cv.yaml`
- **LaTeX tips**: Use `$\sim$` for tilde (~), `\parbox[t]{3.5in}{...}` for multi-line entries in tables
