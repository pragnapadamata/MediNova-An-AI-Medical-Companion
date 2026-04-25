:

🩺 MediNova – An AI-Powered Medical Companion
📌 Overview

MediNova is an AI-driven medical assistant that leverages OCR and NLP to extract medicine names from prescriptions and provide intelligent, context-aware answers to health-related queries. It integrates a Retrieval-Augmented Generation (RAG) pipeline to deliver accurate and reliable responses, along with a clean and interactive interface for seamless user experience.

The system is designed to simulate a real-world healthcare assistant capable of processing unstructured medical data and converting it into meaningful insights.

🚀 Features
✅ OCR-Powered Prescription Reader – Extracts medicine names from uploaded images
✅ NLP-Based Medical Q&A – Answers user queries using a curated medical dataset
✅ Medicine Database Search – Retrieves drug details from structured CSV and FAISS index
✅ RAG Pipeline Integration – Combines retrieval and generation for accurate responses
✅ Secure Login System – Basic authentication for user access
✅ Streamlit UI – Lightweight and interactive web interface
🎥 Demo

👉 Demo Video:
Watch Demo Video

🖥️ Interface Preview
<p align="center"> <img src="interface5.png" width="60%" /> </p>

MediNova provides a simple and user-friendly interface where users can easily upload prescriptions or ask medical questions. The system is designed to minimize complexity while maximizing usability, ensuring that even non-technical users can interact comfortably with the AI assistant.

<p align="center"> <img src="interface2.png" width="60%" /> </p>

The prescription upload module allows users to submit medical images, which are processed using OCR technology. The extracted text is cleaned, structured, and passed into the NLP pipeline for further analysis, enabling accurate extraction of medicine names and related information.

<p align="center"> <img src="interface3.png" width="60%" /> </p>

The AI-powered Q&A system enables users to ask health-related questions in natural language. Using a Retrieval-Augmented Generation pipeline, the system fetches relevant medical context and generates intelligent, context-aware responses, improving reliability and accuracy.

<p align="center"> <img src="interface4.png" width="60%" /> </p>

The medicine search system is powered by FAISS, enabling fast semantic search across medical datasets. This ensures quick retrieval of relevant drug information, enhancing response speed and system efficiency.

<p align="center"> <img src="interface6.png" width="60%" /> </p>

Overall, MediNova delivers an end-to-end AI healthcare assistant experience by combining OCR, NLP, and RAG technologies into a unified system that is efficient, scalable, and user-friendly.

🛠️ Tech Stack
🖥️ Frontend
Streamlit – Web-based UI
HTML/CSS – Styling and layout
Lottie.js – Animations (optional)
⚙️ Backend & Processing
Python – Core logic
Pandas – Data processing
FAISS – Vector similarity search
Pickle – Model/data serialization
🧠 AI & NLP
Tesseract OCR – Image text extraction
Hugging Face Transformers – NLP tasks
Sentence Transformers – Semantic embeddings
💾 Storage
CSV – Medical dataset
FAISS Index – Vector database
.env – Environment configuration
🔧 Setup & Installation
📌 Prerequisites
Python 3.8+
pip package manager
Git (optional)
Virtual environment (recommended)
🚀 Installation Steps

1️⃣ Create Virtual Environment

python -m venv rag-env

Activate (Windows)

rag-env\Scripts\activate

Activate (Mac/Linux)

source rag-env/bin/activate

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file and add required API keys and credentials.

4️⃣ Run Application

streamlit run app.py
🎯 Usage
Upload prescription images through UI
Extract medicine information using OCR
Ask medical questions in chatbot interface
Receive AI-generated context-aware responses
📬 Contact

For queries or contributions, reach out to:
Pragna Padamata
📧 pragnasrilalithapadamata@gmail.com

⭐ License

This project is licensed under the MIT License.
