import requests
from tqdm import tqdm
from .utils import load_state, save_state
from .config import STATE_FILE
from .toc_fetcher import fetch_toc, extract_law_links
from .law_downloader import download_law

def main():
    print("Fetching table of contents...")
    toc_xml = fetch_toc()
    state = load_state(STATE_FILE)
    updated = 0

    session = requests.Session()
    for title, link in tqdm(list(extract_law_links(toc_xml)), desc="Checking laws"):
        if download_law(title, link, session, state):
            updated += 1

    save_state(STATE_FILE, state)
    print(f"\n✅ Done. {updated} laws updated.")

if __name__ == "__main__":
    main()
