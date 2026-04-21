# CV Add

Add a new entry to the master CV database.

## Instructions

1. Read the current CV database from `data/cv.yaml`

2. Ask what type of entry to add:
   - Experience (job/role)
   - Project
   - Publication
   - Patent
   - Certification
   - Skill
   - Education

3. Based on the type, gather information systematically:

### For Experience/Projects:

**Basics:**
- Company/organization
- Title/role
- Dates (start - end or "Present")
- Location

**Context:**
- "What problem were you solving or what was the goal?"
- "What was your role and responsibility?"
- "Who did you work with?" (team size, cross-functional partners, reports)
- "What was the business/project context?" (budget, company stage, industry)

**Approach:**
- "What technologies, tools, or methodologies did you use?"
- "What did you build or create?"

**Impact:**
- "What were the measurable outcomes?" (encourage metrics: %, $, time, scale)
- "What was the business/research impact?"
- "What was novel or unique about your approach?"

**For Projects specifically:**
- URL if public
- Why did you do this? (research, personal interest, etc.)

### For Publications:

- Title
- Type: journal or conference
- Venue name
- Date
- URL or DOI
- What was your contribution/role?

### For Patents:

- Title
- Patent number (if granted)
- Date filed/granted
- Status (pending, granted, in review)
- URL

### For Skills:

- Skill name
- Category (programming_languages, machine_learning, cloud_infrastructure, etc.)
- Context: "Where/how have you used this?" (if not obvious from experience entries)

### For Certifications:

- Name
- Issuing organization
- Date

### For Education:

- Institution
- Degree
- Dates
- Highlights or honors

4. **Generate structured entry:**
   - For experience/projects: Draft 2-3 bullet points using "action verb + what + impact" format
   - Suggest relevant tags based on content (e.g., "python", "leadership", "forecasting", "aws")
   - Show the entry to the user for review
   - Note: Additional bullets can be added later or will be merged in from other resumes via `/cv-build`

5. **Confirm and add:**
   - Ask user to review and approve
   - Add the entry to the appropriate section in `data/cv.yaml`
   - Write the updated database back to file
   - Confirm what was added

## Notes

- For experience entries, help craft strong bullet points (action verb + what + impact)
- Suggest relevant tags based on the content
- **Privacy**: Do not include co-author names in publications - only store title, venue, date, and URL
- Encourage quantifiable metrics when describing impact
- Ask clarifying questions if the user's description is vague
