# generatepage.py

import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in the markdown file")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Check if the dir_path_content itself contains a markdown file
    if os.path.isfile(os.path.join(dir_path_content, "index.md")):
        relative_path = "index.md"
        dest_file_path = os.path.join(dest_dir_path, "index.html")
        with open(os.path.join(dir_path_content, relative_path), "r") as md_file:
            markdown_content = md_file.read()
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
        html_content = markdown_to_html_node(markdown_content).to_html()
        title = extract_title(markdown_content)
        final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
        with open(dest_file_path, "w") as html_file:
            html_file.write(final_content)
        print(f"Generated: {dest_file_path}")

    # Recursively handle subdirectories and their markdown files
    for entry in os.listdir(dir_path_content):
        full_entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_entry_path) and full_entry_path.endswith('.md') and entry != "index.md":
            relative_path = os.path.relpath(full_entry_path, dir_path_content)
            dest_file_path = os.path.join(dest_dir_path, Path(relative_path).with_suffix('.html'))
            if not os.path.exists(dest_file_path):
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                with open(full_entry_path, "r") as md_file:
                    markdown_content = md_file.read()
                with open(template_path, "r") as template_file:
                    template_content = template_file.read()
                html_content = markdown_to_html_node(markdown_content).to_html()
                title = extract_title(markdown_content)
                final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
                with open(dest_file_path, "w") as html_file:
                    html_file.write(final_content)
                print(f"Generated: {dest_file_path}")
        elif os.path.isdir(full_entry_path):
            new_dest_dir_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_entry_path, template_path, new_dest_dir_path)
