import os

MESH_BACKSTAGE_FOLDER_PATH = os.path.join(os.path.dirname(os.getcwd()), 'cosmos', 'data-mesh', 'docs')
print(f"Searching in folder: {MESH_BACKSTAGE_FOLDER_PATH}")

def read_md_files(folder_path):
    md_contents = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Found markdown file: {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    md_contents[file_path] = f.read()
    return md_contents

md_files = read_md_files(MESH_BACKSTAGE_FOLDER_PATH)
print(f"Total markdown files found: {len(md_files)}")

for path, content in md_files.items():
    print(content)
