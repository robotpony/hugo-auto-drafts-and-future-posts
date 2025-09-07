# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a command-line utility that converts CSV output from `hugo list drafts` into a simple HTML list. The tool:
- Reads CSV data from stdin
- Parses Hugo draft metadata (path, slug, title, date, permalink, etc.)
- Outputs an HTML unordered list with links to each draft

## Expected CSV Format

Input CSV must have these headers:
```
path,slug,title,date,expiryDate,publishDate,draft,permalink,kind,section
```

## Output Format

Generate a simple HTML structure:
- `<ul>` containing `<li>` elements
- Each `<li>` should contain an `<a>` tag linking to the permalink with the title as text

## Implementation Notes

When implementing this utility:
- Read CSV from stdin
- Parse CSV headers to map columns correctly
- Handle CSV parsing edge cases (commas in titles, quotes, etc.)
- Output valid HTML to stdout
- Consider making the output minimal but valid HTML (with proper DOCTYPE, head, body tags)

## Development Commands

Once implemented, typical usage will be:
```bash
hugo list drafts | ./hd2html > drafts.html
```

Or if using a scripting language:
```bash
hugo list drafts | python hd2html.py > drafts.html
```