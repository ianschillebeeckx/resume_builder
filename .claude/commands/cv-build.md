# CV Build

Build or update the master CV database from existing resume documents.

## Instructions

1. Read all resume files from `input/resumes/`
2. Read the current CV database from `data/cv.yaml`
3. For each resume, extract:
   - Contact information
   - Work experience (company, title, dates, location, bullet points)
   - Education
   - Skills (categorize as languages, frameworks, tools, other)
   - Projects
   - Certifications
4. Merge extracted data into the CV database:
   - Deduplicate entries (same company + title + dates = same job)
   - Preserve existing entries, add new ones
   - Combine bullet points from multiple versions of the same role
5. Add relevant tags to experience entries based on content (e.g., "python", "leadership", "aws")
6. Write the updated database back to `data/cv.yaml`
7. Summarize what was added/updated

## Notes

- Prefer more detailed descriptions when merging duplicates
- Ask for clarification if dates or details conflict between resumes
- Keep bullet points concise but preserve technical details
