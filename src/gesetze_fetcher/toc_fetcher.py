import requests
from lxml import etree
from .config import TOC_URL, USER_AGENT

def fetch_toc():
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(TOC_URL, headers=headers, timeout=60)
    resp.raise_for_status()
    return etree.fromstring(resp.content)

def extract_law_links(toc_xml):
    # Each <item><link>…</link></item> that ends with xml.zip
    for item in toc_xml.findall(".//item"):
        link = item.findtext("link")
        title = item.findtext("title")
        if link and link.lower().endswith("xml.zip"):
            yield title, link
