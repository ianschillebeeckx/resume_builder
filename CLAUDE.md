# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Resume Builder - a skill-based system for generating tailored LaTeX resumes from a master CV database.

## High-Level Strategy

### Phase 1: Build the CV Database
Generate a comprehensive "master CV" from existing resumes. This is the verbose, complete record of all experience, skills, education, publications, and patents. The database accumulates detail over time - different resumes may describe the same role with different focus areas (technical vs leadership), and all perspectives are preserved.

### Phase 2: Generate Tailored Resumes
Given a job posting (saved locally from a URL) and the CV database, generate an applicable 1-page LaTeX resume. The generation process:
1. Analyzes job requirements and keywords
2. Selects relevant experience entries from the CV database
3. Chooses bullets that best match the role (technical, leadership, etc.)
4. Adapts terminology to match job posting language
5. Outputs LaTeX using the template

## Workflow

1. **CV Database** (`data/cv.yaml`) - Master record of all experience, skills, education
2. **Job Postings** (`input/jobs/`) - Saved job descriptions to tailor resumes for
3. **Resume Generation** - Match CV entries to job requirements → LaTeX output

## Directory Structure

- `.claude/commands/` - Claude Code skills
- `data/cv.yaml` - Master CV database (YAML)
- `templates/` - LaTeX resume templates
- `input/resumes/` - Source resumes for building the CV database
- `input/jobs/` - Saved job postings
- `output/` - Generated resumes

## Skills

- `/cv-build` - Parse existing resumes → build/update CV database
- `/cv-add` - Add new experience/skill entry to database
- `/job-save` - Fetch job posting from URL → save locally
- `/resume-generate` - Generate tailored LaTeX resume from CV + job posting

## LaTeX

Output resumes use LaTeX. Compile with:
```bash
pdflatex output/resume.tex
```

## Design Decisions

- **Terminology**: CV database uses precise, verbose language (e.g., "Revenue Cycle Management (RCM)"). The resume-generate skill adapts terminology to match job posting language. If this becomes unwieldy, consider adding a `terminology` section to map concepts to aliases.

- **Additive Merging**: When building the CV database from multiple resumes, add verbosity rather than replace. Different resumes may emphasize different aspects of the same role (technical skills vs leadership). Keep all bullet variations - the resume-generate skill will select appropriate ones later.

- **Stable vs Dynamic Sections**:
  - Stable (rarely change): contact, education, publications, patents, miscellaneous
  - Dynamic (accumulate): experience bullets, skills, projects

- **Conflict Handling**: If the same role appears with different titles or date ranges across resumes, ask for clarification before updating.

- **Privacy**: Do not include co-author names in publications - only store title, venue, date, and URL. This avoids exposing other people's names in the repository.

## CV Database Structure

The `data/cv.yaml` file contains:
- `_metadata`: Tracks which resumes have been parsed
- `contact`: Name, email, phone, location, LinkedIn, GitHub
- `summary`: Professional summary
- `experience`: List of roles with company, title, dates, location, bullets
- `education`: Degrees with institution, dates, highlights
- `skills`: Categorized (programming, ML, statistics, cloud, bioinformatics, etc.)
- `publications`: Academic papers with type (journal/conference), venue, date, URL
- `patents`: IP with status and URLs
- `certifications`: Professional certifications
- `miscellaneous`: Other info (citizenship, languages, hardware experience)
