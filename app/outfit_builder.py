from app.trend_parser import generate_outfit
from app.product_scraper import scrape_products

def build_outfit_response(trend_name: str, max_products_per_item: int = 3) -> dict:
    """
    Given a trend name, generate a wearable outfit and suggest real products.
    Returns a structured dictionary.
    """
    outfit_text = generate_outfit(trend_name)
    products = scrape_products(outfit_text, max_per_item=max_products_per_item)
    return {
        "trend": trend_name,
        "outfit": outfit_text,
        "products": products
    }