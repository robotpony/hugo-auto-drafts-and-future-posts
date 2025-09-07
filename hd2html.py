#!/usr/bin/env python3
"""Convert Hugo draft CSV output to HTML or Markdown."""

import sys
import csv
import argparse
from datetime import datetime
from html import escape


def parse_date(date_str):
    """Parse ISO format date string."""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y')
    except:
        return date_str


def generate_html(drafts, title="Hugo Drafts"):
    """Generate HTML from draft data."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin: 15px 0;
            padding: 10px;
            background: #f9f9f9;
            border-left: 3px solid #4a90e2;
        }}
        a {{
            color: #2c5282;
            text-decoration: none;
            font-weight: 500;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .date {{
            color: #666;
            font-size: 0.9em;
            margin-left: 10px;
        }}
        .section {{
            color: #888;
            font-size: 0.85em;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <h1>{escape(title)} ({len(drafts)} items)</h1>
    <ul>
"""
    
    for draft in drafts:
        title = escape(draft['title'])
        permalink = escape(draft['permalink'])
        date = parse_date(draft['publishDate'])
        section = escape(draft.get('section', ''))
        
        html += f"""        <li>
            <a href="{permalink}">{title}</a>
            <span class="date">{date}</span>
            {f'<span class="section">[{section}]</span>' if section else ''}
        </li>
"""
    
    html += """    </ul>
</body>
</html>"""
    
    return html


def generate_markdown(drafts, title="Hugo Drafts"):
    """Generate Markdown from draft data."""
    markdown = f"# {title}\n\n"
    markdown += f"*{len(drafts)} draft{'s' if len(drafts) != 1 else ''}*\n\n"
    
    for draft in drafts:
        title_text = draft['title']
        permalink = draft['permalink']
        date = parse_date(draft['publishDate'])
        section = draft.get('section', '')
        
        markdown += f"- [{title_text}]({permalink})"
        markdown += f" *{date}*"
        if section:
            markdown += f" `[{section}]`"
        markdown += "\n"
    
    return markdown


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Convert Hugo draft CSV output to HTML or Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  hugo list drafts | python hd2html.py > drafts.html
  hugo list drafts | python hd2html.py --markdown --title "My Drafts" > drafts.md"""
    )
    parser.add_argument(
        '--markdown', '-m',
        action='store_true',
        help='Output Markdown instead of HTML'
    )
    parser.add_argument(
        '--title', '-t',
        default='Hugo Drafts',
        help='Title for the output (default: "Hugo Drafts")'
    )
    
    args = parser.parse_args()
    
    try:
        reader = csv.DictReader(sys.stdin)
        
        required_fields = {'title', 'permalink', 'publishDate'}
        
        drafts = []
        for row_num, row in enumerate(reader, start=2):
            if row_num == 2:
                missing = required_fields - set(row.keys())
                if missing:
                    print(f"Error: Missing required columns: {', '.join(missing)}", file=sys.stderr)
                    sys.exit(1)
            
            if row.get('draft', '').lower() == 'true':
                drafts.append(row)
        
        drafts.sort(key=lambda x: x['publishDate'], reverse=True)
        
        if args.markdown:
            output = generate_markdown(drafts, args.title)
        else:
            output = generate_html(drafts, args.title)
        
        print(output)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()