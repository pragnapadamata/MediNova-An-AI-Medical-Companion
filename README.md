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
### Upload Image Demo
https://github.com/pragnapadamata/MediNova-An-AI-Medical-Companion/blob/main/assets/UploadImage.mp4

### Demo Video
[Watch Demo Video](assets/UploadImage.mp4)



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

2️⃣ Create & Activate a Virtual Environment

bash
# Create virtual environment  
python -m venv rag-env  
# Activate (Windows)  
rag-env\Scripts\activate  
# Activate (Mac/Linux)  
source rag-env/bin/activate  
3️⃣ Install Dependencies

bash
pip install -r requirements.txt  
4️⃣ Set Up Secrets (if applicable) Add any API keys or credentials in a .env file. 5️⃣ Run the Application

bash
streamlit run app.py  
🎯 Using the Features
bash
# Login System  
python login.py  
# Upload Prescription  
Use the Streamlit UI to upload images  
# Ask Medical Questions  
Use the chatbot interface to query health-related topics  
🎯 Additional Notes
To deactivate the virtual environment, run:

bash
deactivate  
If you face missing dependencies, manually install them:

bash
pip install some_package_name  
🚀 Deployment
Streamlit Cloud / Hugging Face Spaces
Push your code to GitHub

Connect your repo to Streamlit Cloud or Hugging Face Spaces

Set up secrets and environment variables

Deploy and share your app!

📬 Contact
For queries or contributions, reach out to Pragna Padamata at pragnasrilalithapadamata@example.com
