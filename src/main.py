import os
import shutil
from textnode import TextNode
from htmlnode import LeafNode

def dir_copy(src_dir, dest_dir):
    if os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    for entry in os.listdir(src_dir):
        src_path = os.path.join(src_dir, entry)
        dest_path = os.path.join(dest_dir, entry)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file {src_path} to {dest_path}")
        elif os.path.isdir(src_path):
            dir_copy(src_path, dest_path)

def main():
    static = "static"
    public = "public"
    dir_copy(static, public)

if __name__ == "__main__":
    main()

