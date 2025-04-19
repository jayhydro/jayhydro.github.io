# scripts/update_citations.py

import yaml
from scholarly import scholarly, ProxyGenerator

# # (Optional) Set up a free proxy to reduce chance of IP blocking
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

# Your Google Scholar user ID
AUTHOR_ID = "raNrs0gAAAAJ"

# Search by ID and fill author profile
author = scholarly.search_author_id(AUTHOR_ID)
author_filled = scholarly.fill(author)

# Extract total citation count (key "citedby")
total_citations = author_filled.get("citedby", 0)

# Write the count into Jekyll’s data folder
with open("_data/citations.yml", "w", encoding="utf-8") as f:
    yaml.dump({"total_citations": total_citations}, f)

print(f"Total citations updated: {total_citations}")
