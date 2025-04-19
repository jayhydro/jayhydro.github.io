#!/usr/bin/env python3
import sys
import signal
import yaml
from scholarly import scholarly, ProxyGenerator

# ┌───────────────┐
# │ Timeout setup │
# └───────────────┘
class FetchTimeout(Exception):
    pass

def _timeout_handler(signum, frame):
    raise FetchTimeout("Scholar fetch timed out")

# Install our alarm handler and schedule a 30s timeout
signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(30)

# Attempt to set up a free proxy; continue even if it fails
pg = ProxyGenerator()
try:
    pg.FreeProxies()
    scholarly.use_proxy(pg)
    print("✅ Proxy enabled", flush=True)
except Exception as e:
    print(f"⚠️ Proxy setup failed: {e}; continuing without proxy", flush=True)

# Your Google Scholar user ID
AUTHOR_ID = "raNrs0gAAAAJ"

try:
    print("▶️ Starting Scholar fetch...", flush=True)
    author = scholarly.search_author_id(AUTHOR_ID)
    print("✔️ Author retrieved; filling details...", flush=True)
    author_filled = scholarly.fill(author)
    print("✔️ Details filled; extracting citation count...", flush=True)
except FetchTimeout as e:
    print(f"⏱️ {e}; exiting early", flush=True)
    sys.exit(0)
finally:
    # disable the alarm so it doesn't fire later
    signal.alarm(0)

# Extract and write the count
total_citations = author_filled.get("citedby", 0)
with open("_data/citations.yml", "w", encoding="utf-8") as f:
    yaml.dump({"total_citations": total_citations}, f)
print(f"✔️ Citation count written: {total_citations}", flush=True)
