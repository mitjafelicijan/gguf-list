import json
import requests

API_ENDPOINT = "https://huggingface.co/api"
NAMESPACE = "GGUF-Models"

def get_all_collections(namespace):
    base_url = "{API_ENDPOINT}/collections"

    response = requests.get(base_url, params={
        "limit": 100,
        "offset": 0,
        "owner": namespace,
    })

    if response.status_code == 200:
        return response.json()

def get_single_collection(slug):
    url = f"{API_ENDPOINT}/collections/{slug}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None

    collection = response.json()
    for item in collection["items"]:
        print(f" > {item['id']}")

        url = f"{API_ENDPOINT}/models/{item['id']}"
        response = requests.get(url)

        if response.status_code == 200:
            meta = response.json()
            item["files"] = meta["siblings"]
    return collection


all_collections = []
collections = get_all_collections(NAMESPACE)
if collections:
    for collection in collections:
        print(collection["slug"])
        collection = get_single_collection(collection["slug"])
        all_collections.append(collection)

with open("collections.json", "w", encoding="utf-8") as f:
    json.dump(all_collections, f)

