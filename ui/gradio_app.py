import gradio as gr
from app.trend_parser import generate_outfit
from app.product_scraper import scrape_products

def predict_outfit(trend):
    try:
        outfit_text = generate_outfit(trend)
        products = scrape_products(outfit_text)
        product_list = "\n".join(
            [f"- [{p['title']}]({p['url']})" for p in products]
        )
        response = f"### 🧥 Outfit Idea:\n{outfit_text}\n\n### 🛍 Product Suggestions:\n{product_list}"
        return response
    except Exception as e:
        return f"❌ Error: {str(e)}"

interface = gr.Interface(
    fn=predict_outfit,
    inputs=gr.Textbox(lines=1, placeholder="Enter a fashion trend (e.g., quiet luxury)", label="High-Fashion Trend"),
    outputs=gr.Markdown(label="Wearable Outfit + Shopping Links"),
    title="Runway-at-Home: Trend Translator",
    description="Enter a high-fashion trend and get a wearable, affordable outfit suggestion with real product links using LLaMA + Chroma + Google.",
    examples=["quiet luxury", "metallic fringe", "y2k reboot"]
)

if __name__ == "__main__":
    interface.launch()