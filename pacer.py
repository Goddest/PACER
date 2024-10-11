#!/usr/bin/env python3

import os

include_extensions = {
    '.py', '.js', '.java', '.c', '.cpp', '.h', '.cs', '.rb', '.go', '.rs', '.php',
    '.html', '.css', '.xml', '.json', '.sql', '.sh', '.bat', '.ps1', '.conf', '.cfg',
    '.ini', '.yaml', '.yml', '.toml', '.env', '.properties'
}

exclude_extensions = {
    '.exe', '.dll', '.so', '.class', '.o', '.obj', '.pyc', '.pyo', '.pyd', '.jar', '.war',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.mp3', '.mp4', '.avi',
    '.zip', '.rar', '.tar', '.gz', '.7z', '.log', '.tmp', '.bak'
}

exclude_dirs = {
    'node_modules', 'build', 'dist', 'bin', 'obj', '.git', '.svn', '.hg', '__pycache__'
}

def is_included_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() in exclude_extensions:
        return False
    if ext.lower() in include_extensions:
        return True
    return False

def is_excluded_dir(dir_name):
    return dir_name in exclude_dirs

def collect_files(root_dir):
    collected_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not is_excluded_dir(d)]
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_included_file(file_path):
                collected_files.append(file_path)
    return collected_files

def main():
    root_dir = os.getcwd()
    files = collect_files(root_dir)
    for file_path in files:
        relative_path = os.path.relpath(file_path, root_dir)
        print(f"File: {relative_path}")
        print("<begin>")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f.read())
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                print(f.read())
        print("<end>\n")

if __name__ == "__main__":
    main()

