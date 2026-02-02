# Job Save

Fetch a job posting from a URL and save it locally.

## Arguments

$ARGUMENTS - URL of the job posting

## Instructions

1. Fetch the job posting from the provided URL using WebFetch
2. Extract the key information:
   - Job title
   - Company name
   - Location
   - Job description
   - Requirements/qualifications
   - Nice-to-haves (if listed)
3. Save to `input/jobs/` as a markdown file
   - Filename: `{company}-{title}.md` (slugified, lowercase)
   - Include the source URL at the top
   - Preserve the full job description
4. Confirm the file was saved and summarize the role

## Example

```
/job-save https://example.com/jobs/senior-engineer
```

Saves to: `input/jobs/example-senior-engineer.md`
