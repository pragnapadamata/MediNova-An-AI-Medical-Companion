📌 Overview
MediNova is an AI-powered healthcare platform that combines Computer Vision, OCR, multimodal fusion, and local LLM inference to deliver fast, accurate, and secure access to medicine information. It supports image-based medicine identification, fuzzy text search, and a Retrieval-Augmented Generation (RAG) chatbot for structured medical responses.

🚀 Features
✅ AI-driven medicine identification from images ✅ OCR-based label extraction using Tesseract ✅ Multimodal fusion with aleMixMiDa-v2 ✅ Fast similarity search via Faiss ✅ Local LLM inference using Ollama (Mistral) ✅ Fuzzy medicine name matching with RapidFuzz ✅ RAG-based chatbot for structured medical Q&A ✅ Gemini API fallback for general conversations ✅ Privacy-first architecture with local inference ✅ Modular Flask backend with clean API endpoints

🧠 Tech Stack Highlights
Layer	Tools & Libraries
Web Framework	Flask
AI & NLP	SentenceTransformer, Faiss, Ollama (Mistral), RapidFuzz
OCR & Imaging	pytesseract, PIL
Chat Fallback	Gemini API
Data	CSV-based medicine info index
🔄 How It Works
🧬 Medicine RAG System
CSV of medicine info → Full-text fusion → Embeddings → Faiss index

User query → Embedding → Top-k retrieval → Ollama generates structured answer

🔍 Fuzzy Search
User types medicine name → RapidFuzz finds closest match → Returns structured info (Uses, Side Effects, Composition)

🖼️ Image Upload
User uploads medicine image → OCR extracts text → Fuzzy match → Returns structured info

💬 Gemini Fallback
For greetings or casual chat → Gemini API generates friendly replies

🔗 API Endpoints
Endpoint	Description
/	Home page
/chatbot	Chatbot UI
/upload_image	Upload medicine image → OCR + fuzzy match
/send_message	Main chat route → RAG or Gemini fallback
🛠️ Setup & Installation
📌 Prerequisites
Python 3.8+

pip

Git (optional)

Virtual Environment (recommended)

API keys for Gemini (if used)

🚀 Installation Steps
bash
# Clone the repo
git clone https://github.com/your-username/MediNova.git
cd MediNova

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
🔐 Secrets
Add your API keys and credentials to secrets.toml or .env as needed.

▶️ Running the App
bash
# Start the Flask server
python app.py
🎯 Usage
bash
# Medicine Scanner
POST /upload_image

# Chatbot
POST /send_message

# Fuzzy Search
GET /chatbot?medicine=paracetamol
📬 Contact
For questions, collaborations, or contributions, reach out to Pragna Padamata at your-email@example.com.
