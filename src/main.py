# main.py

import os
from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive

def main():
    static_dir = "static"
    public_dir = "public"
    content_path = "content"
    template_path = "template.html"
    dest_dir_path = public_dir  
    generate_pages_recursive(content_path, template_path, dest_dir_path)
    copy_files_recursive(static_dir, public_dir)

if __name__ == "__main__":
    main()

