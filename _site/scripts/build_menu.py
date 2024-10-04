import os

def iter_files(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.qmd'):
                yield os.path.relpath(os.path.join(root, file), path)

categories = [
    {"text": os.path.splitext(file)[0].capitalize(), "href": f"category/{file}"}
    for file in iter_files('category')
]

print(categories)
