#!/usr/bin/python3
""" Convert Markdown file to HTML file. """
import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the content of the Markdown file
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML (simple implementation)
    html_content = "<html><body>" + markdown_content + "</body></html>"

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

    # Print success message
    print(f"Markdown content from {markdown_file} successfully converted to HTML and saved in {output_file}")
    sys.exit(0)


if __name__ == "__main__":
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
