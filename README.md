
# 🧥 Runway-at-Home: Translating Fashion Week into Everyday Wear

**Runway-at-Home** is a fashion-forward AI stylist that transforms high-fashion runway trends into wearable, affordable outfits. By combining Meta's LLaMA-3-8B-Instruct model with Retrieval-Augmented Generation (RAG), product scraping, and a stylish Gradio interface, this app bridges the gap between couture and your closet.

---

## 🌐 Try it Live

▶️ **[Launch on Hugging Face Spaces](https://huggingface.co/spaces/your-username/runway-at-home)**  
*(Replace with your actual URL once deployed)*

---

## ✨ Features

- 🧠 **LLM-Powered Trend Parsing**: Interprets fashion week themes into styling tags.
- 📚 **RAG Engine**: Retrieves relevant fashion advice and aesthetic descriptors.
- 🛍️ **Product Scraping**: Finds affordable fashion alternatives from live e-commerce sites.
- 💁 **Gradio UI**: Lets users interactively explore trends and receive outfit suggestions.
- 📏 **Evaluation Module**: Computes BLEU and ROUGE scores against curated references.

---

## 🗂️ Project Structure

```
.
├── app/                         # Core backend logic (LLM, RAG, scraping)
│   ├── trend_parser.py          # Trend → wearable description (LLM prompting)
│   ├── rag_module.py            # Retrieval from local trend knowledge base
│   ├── product_scraper.py       # Scrape/search affordable fashion products
│   ├── outfit_builder.py        # Assembles outfit suggestion + links
│   └── __init__.py
│
├── data/                        # Data files
│   ├── trends_corpus.csv        # Curated trend blurbs (for RAG)
│   ├── product_samples.json     # Sample product outputs (for testing)
│   └── prompts_examples.json    # For evaluation or reproducibility
│
├── ui/                          # Interfaces
│   ├── gradio_app.py            # Gradio demo interface
│   ├── cli.py                   # CLI for local run: python cli.py "metallic fringe"
│   └── streamlit_app.py         # (Optional) for Streamlit if needed
│
├── eval/                        # Evaluation scripts and metrics
│   ├── metrics.py               # BLEU, ROUGE, relevance score functions
│   ├── eval_samples.json        # Human-labeled or baseline comparisons
│   └── evaluation_report.md     # Qualitative + quantitative analysis
│
│
├── tests/                       # Unit or manual test scripts
│   ├── test_scraper.py
│   ├── test_rag.py
│   └── test_parser.py
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project summary + usage instructions
├── run_tests.sh                       # Shortcut bash script (optional)
├── huggingface_space_link.txt  # (Optional) link to hosted demo
├── LICENSE                      # (Optional) open-source license
├── .gitignore
└── submission/                  # Docs for BAX-493A submission
    ├── technical_summary.pdf
    ├── business_brief.pdf
    └── screenshots/             # UI/Output screenshots for your write-up



```

---

## 🚀 Getting Started (Locally)

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/runway-at-home.git
cd runway-at-home
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scriptsctivate` on Windows
pip install -r requirements.txt
```

### 3. Run the App

```bash
python ui/gradio_app.py
```

---

## 📊 Evaluation

We include curated trend prompts and human-written outfit references to evaluate the model’s creativity and relevance.

### 📁 Input: `eval/eval_samples.json`

```json
[
  {
    "trend": "quiet luxury",
    "reference": "A cashmere sweater in muted beige, tailored wide-leg pants, and minimalist leather flats."
  },
  {
    "trend": "y2k reboot",
    "reference": "Baby tee, low-rise jeans, butterfly clips, and platform sneakers."
  }
]
```

### 🔍 Run Evaluation

```bash
python eval/evaluate_outputs.py
```

### 📈 Sample Output

```
🔹 Trend: y2k reboot
📏 BLEU: 0.47 | ROUGE-1: 0.61 | ROUGE-L: 0.58
📖 Ref: Baby tee, low-rise jeans, butterfly clips, and platform sneakers.
✨ Gen: A baby tee with cargo jeans, sparkly clips, and platform boots.
```

---

## 🧩 Tech Stack

- **Model**: `meta-llama/Meta-Llama-3-8B-Instruct` (via Hugging Face Transformers)
- **RAG**: `sentence-transformers`, `faiss-cpu`
- **Web UI**: `Gradio`
- **Scraping**: `requests`, `beautifulsoup4`
- **Evaluation**: `nltk`, `rouge-score`

---

## 📌 Requirements

```
transformers
gradio
torch
faiss-cpu
sentence-transformers
beautifulsoup4
scikit-learn
rouge-score
nltk
chromadb
gradio
googlesearch-python
```

---

## 📄 License

MIT License

---

## 👩‍💻 Author

**Karishma Mehta**  
MSBA @ UC Davis | Fashion Tech + AI

---

## 🌱 Future Work

- [ ] Add image-to-outfit pipeline using CLIP
- [ ] Integrate outfit preview visualization (via PIL or Canva API)
- [ ] Extend to men’s and non-binary fashion segments
- [ ] Add personalization (body type, climate, budget)

---

## 🖼️ Sneak Peek

> *(Optional)* Add a screenshot of your Gradio interface here:
```
![App Screenshot](assets/example_inputs/sample_ui.png)
```
