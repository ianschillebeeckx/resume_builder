# Job Save

Save a job posting locally from a URL and the verbatim job description.

## Arguments

$ARGUMENTS - URL of the job posting

## Instructions

1. For LinkedIn URLs, fetch the verbatim JD using curl:
   ```
   curl -s -L -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" "URL" | sed -n '/<div class="show-more-less-html__markup/,/<\/div>/p' | sed 's/<[^>]*>//g' | sed '/^$/d'
   ```
   This returns the full verbatim job description text from LinkedIn's public view.
2. For non-LinkedIn URLs, try curl with similar approach or ask the user to paste the verbatim JD.
3. If the user has already provided the verbatim JD text in the conversation, prefer that over the fetched result.
4. Save to `input/jobs/` as a markdown file
   - Filename: `{company}-{title}.md` (slugified, lowercase)
   - Include metadata header (company, location, salary, source URL)
   - Include the full verbatim JD for all description, responsibilities, and qualifications sections
5. Confirm the file was saved and summarize the role

## Example

```
/job-save https://www.linkedin.com/jobs/view/1234567890/
```

Fetches the full verbatim JD via curl and saves it.

Saves to: `input/jobs/example-senior-engineer.md`
