# Hugo drafts to HTML/Markdown

A smol utility to turn some very specific CSV to HTML or Markdown, the output of the `hugo list drafts` converted to simple HTML or Markdown for a sort of local draft view.

## Input (stdin)

```
path,slug,title,date,expiryDate,publishDate,draft,permalink,kind,section
content/blog/2025/from-architect-to-product-leader-and-back.md,from-architect-to-product-leader-and-back,From Architect to Product Leader and Back,2025-07-31T19:54:02-07:00,0001-01-01T00:00:00Z,2025-07-31T19:54:02-07:00,true,https://warpedvisions.org/blog/2025/from-architect-to-product-leader-and-back/,page,blog
content/blog/2025/from-statistical-models-to-ai.md,from-statistical-models-to-ai,From statistical models to AI,2025-07-31T14:17:47-07:00,0001-01-01T00:00:00Z,2025-07-31T14:17:47-07:00,true,https://warpedvisions.org/blog/2025/from-statistical-models-to-ai/,page,blog
content/blog/2025/story-time-how-product-thinking-made-me-a-better-engineer.md,story-time-how-product-thinking-made-me-a-better-engineer,Story time: How product thinking made me a better engineer,2025-07-23T12:22:07Z,0001-01-01T00:00:00Z,2025-07-23T12:22:07Z,true,https://warpedvisions.org/blog/2025/story-time-how-product-thinking-made-me-a-better-engineer/,page,blog
content/blog/2025/the-hidden-world-principle-why-great-software-reveals-itself.md,the-hidden-world-principle-why-great-software-reveals-itself,The hidden world principle: why great software reveals itself slowly,2025-01-27T00:00:00Z,0001-01-01T00:00:00Z,2025-01-27T00:00:00Z,true,https://warpedvisions.org/blog/2025/the-hidden-world-principle-why-great-software-reveals-itself/,page,blog
content/blog/2025/beware-of-turducken-projects.md,beware-of-turducken-projects,Beware of turducken projects,2024-12-27T12:00:00Z,0001-01-01T00:00:00Z,2024-12-27T12:00:00Z,true,https://warpedvisions.org/blog/2025/beware-of-turducken-projects/,page,blog
content/blog/2025/the-physics-hidden-in-your-codebase.md,the-physics-hidden-in-your-codebase,The physics hidden in your codebase,2024-12-27T12:00:00Z,0001-01-01T00:00:00Z,2024-12-27T12:00:00Z,true,https://warpedvisions.org/blog/2025/the-physics-hidden-in-your-codebase/,page,blog
content/blog/2025/when-technology-gets-boring-innovation-begins.md,when-technology-gets-boring-innovation-begins,"When technology gets boring, innovation begins",2024-12-27T12:00:00Z,0001-01-01T00:00:00Z,2024-12-27T12:00:00Z,true,https://warpedvisions.org/blog/2025/when-technology-gets-boring-innovation-begins/,page,blog
content/blog/2025/after-the-prompt-how-ai-disappears-into-everything.md,after-the-prompt-how-ai-disappears-into-everything,After the prompt: how AI disappears into everything,2024-12-24T10:00:00Z,0001-01-01T00:00:00Z,2024-12-24T10:00:00Z,true,https://warpedvisions.org/blog/2025/after-the-prompt-how-ai-disappears-into-everything/,page,blog
```

## Usage

```bash
# Default: HTML output
hugo list drafts | python hd2html.py > drafts.html

# Markdown output
hugo list drafts | python hd2html.py --markdown > drafts.md

# Custom title
hugo list drafts | python hd2html.py --title "My Blog Drafts" > drafts.html

# Markdown with custom title
hugo list drafts | python hd2html.py -m -t "Development Drafts" > drafts.md
```

## Options

- `--markdown`, `-m`: Output Markdown instead of HTML
- `--title TITLE`, `-t TITLE`: Set a custom title (default: "Hugo Drafts")
- `--draft`: Mark the generated markdown as draft (default: true)
- `--help`, `-h`: Show help message

## Output Formats

### HTML Output
A styled HTML page with:
- Responsive design with clean typography
- A title showing the draft count
- An unordered list of drafts with links, dates, and sections
- Sorted by publish date (newest first)

### Markdown Output
A Markdown document with:
- Hugo-compatible YAML frontmatter including:
  - URL-friendly slug generated from title
  - Current timestamp in ISO format
  - Configurable draft status
- Draft count in italics
- Bulleted list with linked titles, dates in italics, and sections in code blocks
- Sorted by publish date (newest first)