# Job Search Tracker — Senior Tech Client Executive, Philadelphia

This folder is a personal job-search tracker for landing a **Senior Tech Client
Executive** (or closely-related enterprise tech account/sales-leadership)
role in the Philadelphia metro area. It's kept in this repo so an automated
weekly search can commit new leads here and you get a durable, versioned
record instead of a spreadsheet that drifts.

## Files

- `search-criteria.md` — the exact titles, keywords, and target-company list
  the automated search uses. Edit this file to steer future runs.
- `leads.md` — the running table of companies/openings found, with source
  links, dates, and a status column you update as you work each lead.
- (this file) — how the system works.

## How the automation works

A weekly Routine (Claude Code scheduled trigger) fires into a fresh session
that:
1. Clones this repo and checks out `claude/tech-exec-philly-search-iojqdf`.
2. Reads `search-criteria.md` for the target titles/keywords/companies and
   `leads.md` for what's already been found (to avoid duplicates).
3. Runs web searches for new matching postings and hiring signals in the
   Philadelphia area.
4. Appends new, deduplicated rows to `leads.md` (source link included so you
   can verify every entry yourself) and pushes the commit.
5. Sends you a push/email notification summarizing what's new.

**What it will not do:** invent names of hiring managers or claim a posting
exists without a source link. Job boards and company sites don't always
expose a named hiring manager — where one isn't publicly listed, the lead
is logged as "identify contact via LinkedIn" rather than guessed.

## Your part

- Work `leads.md` top to bottom: research the named contact on LinkedIn,
  personalize outreach, and update the `Status` column.
- Update `search-criteria.md` any time you learn a new job title, company,
  or keyword that's converting, so future automated runs target it.
