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
- **Bullet allocation**: More recent/relevant roles get more bullets (3-4), older roles get fewer (2-3)
- **Balance**: Mix direct job matches with excellence indicators (awards, publications, exceptional outcomes)
- **Terminology**: Generalize domain-specific terms to broader applicability where appropriate
  - Example: "clinical validation study" → "prespecified randomized multi-center study"
  - Example: "biomarker" → "production ML model"

### 4. Content Selection Guidelines
- Lead with strongest matches to job requirements
- Emphasize quantified business impact (%, $, time, scale)
- Include cross-functional collaboration and team leadership
- Highlight 0→1 platform/product building where relevant
- Show technical depth through specific methods/tools

### 5. Generate LaTeX Resume
- Use ian-template.tex structure
- Fill Experience section with selected roles and tailored bullets
- Create Technical Skills section with categories ordered by relevance to job
- Include Publications section if research/technical depth is valued
- **Target**: 1 page (adjust bullets if needed to fit)

### 6. Output
- Write to `output/[company]-[role-slug].tex`
- Compile to PDF
- Provide summary of:
  - What was emphasized
  - Key positioning choices
  - Suggested adjustments if needed

## Selection Criteria Examples

**For forecasting/data science leadership roles:**
- Forecasting transformation metrics
- Team size, budget, cross-functional partnerships
- Causal inference, predictive modeling
- Production ML systems
- Executive communication

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
