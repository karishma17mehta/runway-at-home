import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.product_scraper import scrape_products

def test_scrape_products():
    outfit = "linen shirt, knit cardigan"
    products = scrape_products(outfit, max_results=2)
    assert isinstance(products, list)
    assert all("title" in p and "url" in p for p in products)

if __name__ == "__main__":
    test_scrape_products()
    print("✅ Product scraper test passed")