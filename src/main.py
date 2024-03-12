# main.py

import os
from copystatic import copy_files_recursive
from generatepage import generate_page

def main():
    static_dir = "static"
    public_dir = "public"
    content_path = "content/index.md"
    template_path = "template.html"
    dest_path = os.path.join(public_dir, "index.html")
    copy_files_recursive(static_dir, public_dir)
    generate_page(content_path, template_path, dest_path)

if __name__ == "__main__":
    main()

