from googlesearch import search
from urllib.parse import urlparse
import time

    time.sleep(1.5)  # Add a 1.5-second delay between queries
RETAIL_SITES = ["hm.com", "asos.com", "zara.com", "mango.com", "uniqlo.com"]

def real_scrape_products(query_item: str, max_results: int = 3):
    """
    Perform a Google search for a product item across trusted fashion retailers.
    Returns a list of dicts with title and URL.
    """
    product_links = []
    query = f"{query_item} site:" + " OR site:".join(RETAIL_SITES)

    print(f"🔍 Searching Google for: {query}")
    try:
        for url in search(query, num=max_results):
            domain = urlparse(url).netloc
            product_links.append({
                "title": f"{query_item.title()} from {domain}",
                "url": url
            })
    except Exception as e:
        print("⚠️ Google search failed:", e)

    return product_links


def scrape_products(outfit_description: str, max_per_item: int = 3):
    """
    Given a comma-separated outfit description,
    searches real product links for each clothing item.
    """
    outfit_items = [x.strip().lower() for x in outfit_description.split(",")]
    results = []

    for item in outfit_items:
        links = real_scrape_products(item, max_results=max_per_item)
        results.extend(links)

    return results