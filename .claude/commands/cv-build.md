# CV Build

Update the master CV database from a resume document.

## Arguments

$ARGUMENTS - Filename of resume in `input/resumes/`

## Instructions

### Step 1: Gain Context

Read the current CV database from `data/cv.yaml` to understand what's already recorded.

### Step 2: Read the Resume

Read the specified resume from `input/resumes/`.

### Step 3: Update the CV Database

Compare the resume against the existing database and update:

**Stable sections** (rarely change, just fill in if empty):
- Contact information
- Education
- Publications
- Patents
- Miscellaneous

**Dynamic sections** (accumulate verbosity):
- Experience: responsibilities, contributions, technologies, tools
- Projects: descriptions, highlights
- Skills

#### Merging Rules

- **Add, don't replace**: Different resumes may describe the same role with different focus (technical vs leadership). Accumulate all bullet points - the resume-generate skill will select relevant ones later.
- **Be suspicious of conflicts**: If a role appears with a different title or date range, ask for clarification before updating.
- **Preserve nuance**: A bullet about "cross-functional leadership" and one about "implemented microservices architecture" for the same role are both valuable - keep both.
- **Deduplicate carefully**: Only remove bullets that are truly identical, not ones that are similar but emphasize different aspects.

### Step 4: Log and Summarize

After updating `data/cv.yaml`:

1. Add an entry to `_metadata.parsed_resumes` with the filename and today's date
2. Summarize:
   - What was added
   - Any conflicts or questions that need clarification
   - Suggestions for missing information

Note: Check the log before processing - if a resume was already parsed, confirm the user wants to re-process it.

**Privacy**: Do not include co-author names in publications - only store title, venue, date, and URL.

## Example

```
/cv-build resume-2023-google.md
```
