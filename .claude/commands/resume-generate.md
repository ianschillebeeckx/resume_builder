# Resume Generate

Generate a tailored LaTeX resume for a specific job posting.

## Arguments

$ARGUMENTS - (optional) Name of job file in `input/jobs/`, or leave blank to select

## Instructions

1. If no job specified, list available jobs in `input/jobs/` and ask which one
2. Read the job posting file
3. Read the master CV database from `data/cv.yaml`
4. Read the LaTeX template from `templates/`
5. Select and tailor content:
   - Choose experience entries most relevant to the job requirements
   - Prioritize bullets that match job keywords/requirements
   - Reorder skills to lead with most relevant
   - Adjust summary to align with the role
6. Generate the LaTeX resume:
   - Use the template structure
   - Fill in selected/tailored content
   - Keep to 1 page unless otherwise specified
7. Write to `output/` with filename based on company/role
8. Provide a summary of what was emphasized and any suggestions

## Notes

- Match keywords from job description where authentic
- Quantify achievements where possible
- Ask if anything seems missing or should be adjusted
