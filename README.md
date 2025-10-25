# 🩺 MediNova – An AI-Powered Medical Companion

## 📌 Overview
MediNova is an **AI-driven medical assistant** that leverages **OCR and NLP** to extract medicine names from prescriptions and provide intelligent, context-aware answers to health-related queries. It integrates a **retrieval-augmented generation (RAG)** pipeline for accurate responses and features a clean, interactive interface for users to explore medical information.

## 🚀 Features
- ✅ **OCR-Powered Prescription Reader** – Extracts medicine names from uploaded images
- ✅ **NLP-Based Medical Q&A** – Answers user queries using a curated medical dataset
- ✅ **Medicine Database Search** – Retrieves drug details from structured CSV and FAISS index
- ✅ **RAG Pipeline Integration** – Combines retrieval and generation for accurate responses
- ✅ **Secure Login System** – Basic authentication for user access
- ✅ **Streamlit UI** – Lightweight, interactive web interface

## 📸 Screenshots & Videos
### **Home Page**

https://github.com/user-attachments/assets/medinova-homepage-screenshot

### **Prescription Upload**

https://github.com/user-attachments/assets/medinova-upload-screenshot

### **Medicine Details**

https://github.com/user-attachments/assets/medinova-medicine-screenshot

### **Chatbot Interface**
![image](https://github.com/user-attachments/assets/medinova-chatbot-screenshot)

## 🛠️ Tech Stack
**Frontend:**
- ✅ Streamlit – For the web-based UI
- ✅ HTML/CSS – For layout and styling
- ✅ Lottie.js – For animated visuals (optional)

**Backend & Computation:**
- ✅ Python – Core programming language
- ✅ Pandas – For data handling
- ✅ FAISS – For fast similarity search
- ✅ Pickle – For serialized data storage

**AI & NLP:**
- ✅ Tesseract OCR – For text extraction from images
- ✅ Hugging Face Transformers – For question answering
- ✅ Sentence Transformers – For semantic search

**Storage & Data:**
- ✅ CSV – Medicine database
- ✅ FAISS Index – Vector search
- ✅ .env – For secure API keys and environment variables

## 🔧 Setup & Installation

### 📌 Prerequisites
Ensure you have the following installed:
- 🐍 Python 3.8+
- 📦 pip (Python package manager)
- 💻 Git (optional, for cloning)
- 📂 Virtual Environment (recommended)

### 🚀 Installation Steps

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/pragnapadamata/MediNova-An-AI-Medical-Companion.git
cd MediNova-An-AI-Medical-Companion
