# Resume Critique

Analyze a resume from the hiring manager's perspective to identify gaps and improvement opportunities.

## Arguments

$ARGUMENTS - Path to resume .tex file and job posting (e.g., `output/openai-*.tex input/jobs/openai-*.md`)

## Instructions

### 1. Setup
- Read the resume .tex file
- Read the job description
- Understand the role's core requirements and what a hiring manager would prioritize

### 2. Critique as Technical Hiring Manager

Analyze from the perspective of a data scientist or technical leader who would be hiring for this role:

**Depth Check**
- Does the resume show enough examples for the core role focus?

**Specificity Check**
- Are metrics vague or concrete?
- e.g "Product volume" vs "unit volume driving $270M revenue"
- e.g "Improved model" vs "reduced error from 6% to 0.9%"

**Domain Gap Check**
- Would a tech hiring manager understand the terminology?
- Flag clinical/healthcare jargon that doesn't translate
- Suggest universal alternatives (e.g., "historically controlled" → "pre-post controlled analysis")

**Platform vs Model Check**
- Does it show reusable systems or just one-off projects?
- Look for: dashboards, tools others adopted, infrastructure

**Monitoring/Production Check**
- Any evidence of model maintenance, drift detection, retraining?
- Production ML roles care deeply about this

**Methods Currency Check**
- Are the methods listed current or dated for the field?
- Look for modern approaches where applicable

**Cross-Functional Check**
- Does it show executive communication and influence?
- Who did they partner with? (CEO/CFO/COO vs just engineering)

### 3. Output

Provide structured feedback:

```
## Strengths
- [What's working well for this JD]

## Concerns
1. **[Issue name]** - [Explanation and why it matters]
2. ...

## Bottom Line
[1-2 sentence summary of candidacy strength]
```

Then ask which concerns can be addressed with real experience from the CV.

## Notes

- Be direct and objective, not encouraging
- A good critique helps improve the resume, not validate it
- Mention ALL gaps, even those that can't be filled from CV - unfillable gaps help prepare interview talking points
