#!/bin/bash


echo "🚀 Running unit tests for Runway-at-Home..."

echo -e "\n🧠 Testing RAG Module..."
python3 tests/test_rag.py || exit 1

echo -e "\n🎨 Testing Trend Parser (LLM Generation)..."
python3 tests/test_parser.py || exit 1

echo -e "\n🛍️ Testing Product Scraper..."
python3 tests/test_scraper.py || exit 1

echo -e "\n✅ All tests passed!"
