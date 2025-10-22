import os, json, hashlib, zipfile, io

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_state(path: str) -> dict:
    if not os.path.exists(path):
        return {"laws": {}, "toc": {}}
    with open(path, "r") as f:
        return json.load(f)

def save_state(path: str, state: dict):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)

def unzip_bytes(content: bytes, out_dir: str):
    with zipfile.ZipFile(io.BytesIO(content)) as zf:
        zf.extractall(out_dir)
