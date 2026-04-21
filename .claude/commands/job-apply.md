---
name: job-apply
description: >
  [REQUIRES CLAUDE COWORK - needs browser/computer use to interact with web forms]
  Apply to job postings by filling out online application forms on ATS platforms (Greenhouse, Lever, Workday, Ashby, and others).
  Use this skill whenever the user shares a job application URL and asks you to apply, submit an application, fill out a job form,
  or says things like "apply to this job", "fill out this application", "submit my resume to this role". Also trigger when the user
  pastes a URL from greenhouse.io, lever.co, myworkdayjobs.com, or other ATS domains alongside any intent to apply.
  Even if the user just pastes a job URL with minimal context, this skill is likely what they want.
---

# Job Application Skill (Claude Cowork)

> **Note:** This skill requires Claude Cowork (computer use / browser interaction) to fill out web forms. It will not work in Claude Code CLI.

You help the user apply to jobs by filling out online application forms. The workflow has three phases: preparation, form-filling, and review. Never submit the application without explicit user approval.

## Applicant Profile

These details are hardcoded for the applicant. Use them to fill forms without needing to re-read the resume each time.

```
Full Name: Ian Schillebeeckx
First Name: Ian
Last Name: Schillebeeckx
Email: ianschillebeeckx@gmail.com
Phone: 636-667-7425 (US +1)
LinkedIn: https://www.linkedin.com/in/ianschillebeeckx
GitHub: https://github.com/ianschillebeeckx

Location: San Francisco, CA
Work Authorization: US citizen, legally authorized to work in the US
Visa Sponsorship Required: No

EEO / Demographics (voluntary):
  Gender: Male
  Hispanic/Latino: No
  Race: White
  Veteran Status: Not a protected veteran
  Disability: No disability

Education:
  PhD, Computer Science (Machine Learning) - Washington University in St. Louis, 2012-2016
  Honors BS, Computer Science & Honors BS, Applied Mathematics - Saint Louis University, 2007-2011
```

## Phase 1: Preparation

### Find the right resume

Resumes live in the user's mounted folder at the path ending in `resume_builder/output/`. Each resume is a PDF named after the company and role, like `philo-head-of-data.pdf` or `google-data-science-manager-home.pdf`.

1. List the PDF files in the resume output directory.
2. Match the resume to the job by company name and role keywords from the job URL or title. Look for the closest match. If there are multiple plausible matches or no clear match, ask the user which one to use.
3. Read the corresponding `.tex` file (same name, different extension) if you need to extract any details not covered by the hardcoded profile above — for instance, if the application asks questions about specific experience or skills that you'd want to pull from the resume content.

### Open the job posting

1. Get the browser tab context (create a new tab group if needed, then create a new tab).
2. Navigate to the job application URL the user provided.
3. Find and click the "Apply" button to reach the application form.

## Phase 2: Fill Out the Form

The goal is to complete all **mandatory fields** (typically marked with an asterisk `*`) and leave optional fields blank unless the user has indicated they want them filled. Work through the form section by section, scrolling down to discover all fields.

### General approach for any ATS

Every ATS is different, but the general pattern is:

1. **Try uploading the resume first.** Many ATS platforms will auto-populate fields (name, email, phone, LinkedIn) from the resume. Look for a file input for Resume/CV and upload the matched PDF. If the browser blocks the programmatic upload (this is common due to security restrictions), tell the user which file to upload manually and continue filling other fields.

2. **Fill personal info fields** using the hardcoded profile above. If the form was auto-populated (e.g., from a MyGreenhouse/Lever profile), verify the values are correct rather than overwriting them.

3. **Handle dropdowns carefully.** For select/dropdown fields, click to open them and then click the correct option from the visible list. Using `form_input` with text values for dropdowns sometimes doesn't stick — clicking is more reliable. After setting a dropdown, take a screenshot to verify the value was actually saved.

4. **Work authorization & sponsorship questions** — answer based on the profile: authorized = Yes, sponsorship needed = No.

5. **EEO / Demographic / Voluntary Self-Identification sections** — fill using the profile demographics. These are usually optional but the user wants them filled.

6. **Cover letter** — skip unless the user explicitly asks for one.

7. **"How did you hear about this job?"** — skip unless the user specifies.

8. **Salary expectations** — do NOT fill in. Ask the user if the field is mandatory.

9. **Free-text questions** (e.g., "Why do you want to work here?", "Describe your experience with X") — do NOT answer these yourself. Show the question to the user and ask them how they'd like to respond. If you can pull a relevant bullet from the resume `.tex` file, suggest it as a starting point.

### ATS-specific tips

**Greenhouse** (`job-boards.greenhouse.io` or `boards.greenhouse.io`):
- Often has "Autofill with MyGreenhouse" which pre-populates from a saved profile
- Resume upload is under "Resume/CV *" with Attach/Dropbox/Google Drive/Enter manually buttons — use the file input behind the "Attach" button
- Dropdowns for work authorization and sponsorship are custom select elements — click to open, then click the option

**Lever** (`jobs.lever.co`):
- Simpler forms, usually just name/email/phone/resume/LinkedIn
- Resume upload via a file input or drag-and-drop area
- Fewer dropdown fields, more text inputs

**Workday** (`myworkdayjobs.com` or `*.wd5.myworkdayjobs.com`):
- More complex multi-page forms with "Next" buttons between sections
- May require creating an account first — do NOT create accounts on the user's behalf. Flag this to the user.
- Often has separate pages for personal info, experience, education, and voluntary disclosures

**Ashby** (`jobs.ashbyhq.com`):
- Clean single-page forms similar to Greenhouse
- Resume upload via file input

**Other platforms**: Use the general approach. Scan the page for required field markers and fill accordingly.

### When things go wrong

- **File upload blocked**: Tell the user the exact filename and where to find it, then continue filling other fields.
- **Dropdown value won't stick**: Try clicking the dropdown to open it, then clicking the option text directly. If that fails, try `form_input` with the exact option text. Take a screenshot to verify.
- **CAPTCHA or bot detection**: Stop and tell the user they need to complete it manually.
- **Account creation required**: Stop and tell the user — never create accounts on their behalf.
- **Multi-page form**: Work through each page, clicking "Next"/"Continue" after filling required fields. Screenshot each page before advancing.

## Phase 3: Review Before Submission

This is critical — never click "Submit" without the user's go-ahead.

1. Scroll through the entire completed form, taking screenshots of each section.
2. Present a summary of all filled fields to the user, organized by section.
3. Flag anything you're unsure about or couldn't fill.
4. Wait for the user to say they've reviewed it and are ready to submit (or that they've clicked submit themselves).
5. If the user asks you to submit, click the submit button only after explicit confirmation.
