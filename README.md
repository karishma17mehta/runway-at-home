# Runway-at-home

#trend-translator/
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
├── notebooks/                   # Prototyping & exploration
│   ├── trend_prompt_dev.ipynb   # Prompt engineering and tuning
│   ├── rag_test.ipynb           # Retrieval validation
│   └── scraper_demo.ipynb       # Product scraping experiments
│
├── tests/                       # Unit or manual test scripts
│   ├── test_scraper.py
│   ├── test_rag.py
│   └── test_parser.py
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project summary + usage instructions
├── run.sh                       # Shortcut bash script (optional)
├── huggingface_space_link.txt  # (Optional) link to hosted demo
├── LICENSE                      # (Optional) open-source license
├── .gitignore
└── submission/                  # Docs for BAX-493A submission
    ├── technical_summary.pdf
    ├── business_brief.pdf
    └── screenshots/             # UI/Output screenshots for your write-up

#
