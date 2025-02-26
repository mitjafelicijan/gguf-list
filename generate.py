import sys
import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./"))
template = env.get_template("template.html")

with open("collections.json", "r") as f:
    collections = json.load(f)

if not collections:
    sys.exit(1)

files = []
for collection in collections:
    for item in collection["items"]:
        for file in item["files"]:
            if file["rfilename"].endswith(".gguf"):
                files.append({
                    "repository": f"https://huggingface.com/{item['id']}",
                    "url": f"https://huggingface.com/{item['id']}/resolve/main/{file['rfilename']}",
                    "last_modified": item["lastModified"],
                    "author": item["author"],
                })

result = template.render(files=files)
with open("collections.html", "w", encoding="utf-8") as f:
    f.write(result)
