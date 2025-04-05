SHL Assessment Recommendation System

This is a GenAI-powered project that recommends relevant SHL assessments based on a given job description or natural language query. It leverages semantic search using Sentence Transformers and FAISS vector indexing to match job roles with SHL's product catalog.

🔍 Features
🔗 Web Scraper: Scrapes SHL's official product catalog for assessment names, descriptions, and URLs.
📚 Embeddings: Converts assessment descriptions into vector embeddings using sentence-transformers (all-MiniLM-L6-v2).
⚡ FAISS Index: Uses Facebook AI Similarity Search (FAISS) to index and quickly retrieve relevant assessments.
🚀 FastAPI Backend: API endpoint to fetch top-10 recommendations from a job description or query.
🌐 Streamlit Frontend: Clean UI to input text and view assessment recommendations interactively.
🧰 Tech Stack
Python 3.12
BeautifulSoup (for scraping)
Sentence Transformers
FAISS
FastAPI
Streamlit
📦 How to Run
1. Clone this repository

git clone https://github.com/manojyadav0/SHL.git
cd SHL
2. Install dependencies

pip install -r requirements.txt
3. Scrape assessment data

python3 utils/scraper.py
4. Generate embeddings

python3 backend/embeddings.py
5. Run FastAPI backend

uvicorn api:app --reload
6. Run frontend UI

streamlit run frontend.py
