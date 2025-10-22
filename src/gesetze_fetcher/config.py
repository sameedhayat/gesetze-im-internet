import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
DATA_DIR = os.path.join(BASE_DIR, "data/raw")
STATE_FILE = os.path.join(BASE_DIR, "db/state.json")

TOC_URL = "https://www.gesetze-im-internet.de/gii-toc.xml"
USER_AGENT = "gesetze-fetcher/0.1 (+contact@example.org)"
