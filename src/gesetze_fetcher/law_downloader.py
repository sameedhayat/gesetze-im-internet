import os, requests
from tqdm import tqdm
from .config import DATA_DIR, USER_AGENT
from .utils import ensure_dir, sha256_bytes, unzip_bytes

def download_law(short_name: str, url: str, session: requests.Session, state: dict, title: str = ""):
    ensure_dir(DATA_DIR)
    law_dir = os.path.join(DATA_DIR, short_name)
    ensure_dir(law_dir)

    headers = {"User-Agent": USER_AGENT}
    resp = session.get(url, headers=headers, timeout=120)
    resp.raise_for_status()
    content = resp.content
    sha = sha256_bytes(content)

    prev_sha = state["laws"].get(url, {}).get("sha256")
    if prev_sha == sha:
        return False  # unchanged

    zip_path = os.path.join(law_dir, f"{sha}.zip")
    with open(zip_path, "wb") as f:
        f.write(content)
    unzip_bytes(content, law_dir)

    state["laws"][url] = {
        "sha256": sha,
        "short_name": short_name,
        "title": title
    }
    return True

