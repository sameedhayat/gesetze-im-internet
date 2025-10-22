import requests
from lxml import etree
from .config import TOC_URL, USER_AGENT

def fetch_toc():
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(TOC_URL, headers=headers, timeout=60)
    resp.raise_for_status()
    return etree.fromstring(resp.content)

import re

def extract_law_links(toc_xml):
    """Yield (short_name, link, title) tuples for each law in gii-toc.xml."""
    for item in toc_xml.findall(".//item"):
        link = item.findtext("link")
        title = item.findtext("title") or "Unknown"
        if link and link.lower().endswith("xml.zip"):
            # extract the part before /xml.zip
            match = re.search(r'/([^/]+)/xml\.zip$', link)
            if match:
                short_name = match.group(1).strip()
            else:
                # fallback if pattern not found
                short_name = title[:50].replace(" ", "_")
            yield short_name, link, title

