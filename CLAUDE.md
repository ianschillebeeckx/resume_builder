# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Resume Builder - a skill-based system for generating tailored LaTeX resumes from a master CV database.

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
