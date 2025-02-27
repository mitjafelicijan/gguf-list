# GGUF model list

Generated list of available GGUF models on HuggingFace under GGUF-Models
namespace.

- https://huggingface.co/docs/hub/api
- https://huggingface.co/GGUF-Models

> [!IMPORTANT]
> There is not need to run the scripts below. You only do this if you need to
> refresh registry.

```console
python3 -m venv .venv
source .venv/bin/activate
pip install jinja2 requests

python fetchdata.py
python generate.py
python ggufdlprep.py
```

## Easy CLI Model download utility

Requires:

- wget
- dialog

```console
# Debian/Fedora Linux
sudo apt install wget dialog
sudo dnf install wget dialog

# macOS
brew install wget dialog
```

After you can run the utility from terminal with `sh ggufdl.sh`.

https://github.com/user-attachments/assets/54a812df-7dfc-4fe9-a4c8-b5e1bff71c12
