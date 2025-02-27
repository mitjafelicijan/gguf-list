import sys
import json

with open("collections.json", "r") as f:
    collections = json.load(f)

if not collections:
    sys.exit(1)

dialog_file = open("dialog-data.txt", "w", encoding="utf-8")

for collection in collections:
    title = ''.join(char for char in collection["title"] if ord(char) < 128)
    slug = collection["slug"].split("/")[1]
    dialog_file.write(f"c:{title} {slug}\n")

    for item in collection["items"]:
        dialog_file.write(f"m:{title}:{item['id']} {item['downloads']} off\n")
        for file in item["files"]:
            if file["rfilename"].endswith(".gguf"):
                dialog_file.write(f"f:{item['id']} https://huggingface.com/{item['id']}/resolve/main/{file['rfilename']}\n")

dialog_file.close()
