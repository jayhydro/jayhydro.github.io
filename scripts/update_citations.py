#!/usr/bin/env python3
import yaml
from scholarly import scholarly, ProxyGenerator

# Attempt to set up a free proxy; continue even if it fails
pg = ProxyGenerator()
try:
    pg.FreeProxies()
    scholarly.use_proxy(pg)
    print("✅ Proxy enabled")
except Exception as e:
    print(f"⚠️ Proxy setup failed: {e}; continuing without proxy")

# Your Google Scholar user ID
AUTHOR_ID = "raNrs0gAAAAJ"

print("▶️ Starting Scholar fetch...")
author = scholarly.search_author_id(AUTHOR_ID)
print("✔️ Author object retrieved; filling details...")
author_filled = scholarly.fill(author)
print("✔️ Details filled; extracting citation count...")
total_citations = author_filled.get("citedby", 0)

# Write the citation count to Jekyll’s data folder
with open("_data/citations.yml", "w", encoding="utf-8") as f:
    yaml.dump({"total_citations": total_citations}, f)
print(f"✔️ Citation count written: {total_citations}")
