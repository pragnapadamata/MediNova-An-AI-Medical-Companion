

# 🩺 MediNova: Your AI-Powered Medical Companion

**MediNova** is an intelligent healthcare assistant designed to bridge the gap between unstructured medical documents and actionable health insights. By integrating **Optical Character Recognition (OCR)** with a **Retrieval-Augmented Generation (RAG)** pipeline, MediNova transforms prescription images and natural language queries into reliable, context-aware medical information.

---

### 🚀 Key Features

* **✅ OCR Prescription Analysis:** Automatically extracts medicine names and dosages from uploaded handwritten or printed images.
* **✅ RAG-Powered Q&A:** Combines a curated medical knowledge base with LLMs to provide factual, evidence-based answers.
* **✅ Semantic Medicine Search:** Uses **FAISS** for lightning-fast vector searches across extensive drug databases.
* **✅ Interactive Streamlit UI:** A sleek, user-friendly interface designed for both patients and healthcare providers.
* **✅ Secure Access:** Integrated basic authentication to ensure user data privacy.

---

### 🛠️ The Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | Streamlit, HTML5/CSS3, Lottie Animations |
| **Orchestration** | Python, LangChain (RAG Pipeline) |
| **AI/NLP** | Hugging Face Transformers, Sentence Transformers |
| **OCR Engine** | Tesseract OCR |
| **Vector DB** | FAISS (Facebook AI Similarity Search) |
| **Data Handling** | Pandas, NumPy, Pickle |

---

### 📖 System Architecture

MediNova operates on a multi-stage pipeline to ensure accuracy:
1.  **Ingestion:** User uploads an image or types a query.
2.  **Processing:** OCR extracts text; NLP models generate semantic embeddings.
3.  **Retrieval:** The system queries the **FAISS index** to find the most relevant medical context.
4.  **Generation:** An LLM synthesizes the retrieved data into a natural, easy-to-understand response.



---

### 🔧 Installation & Setup

#### 1. Clone & Environment
```bash
# Clone the repository
git clone https://github.com/your-username/medinova.git
cd medinova

# Create a virtual environment
python -m venv rag-env

# Activate (Windows)
rag-env\Scripts\activate
# Activate (Mac/Linux)
source rag-env/bin/activate
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Configuration
Create a `.env` file in the root directory and add your specific configurations:
```env
API_KEY=your_key_here
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

#### 4. Launch
```bash
streamlit run app.py
```

---

### 🎥 Project Previews

> **Note:** The interface is designed to minimize complexity, ensuring accessibility for non-technical users.

| Prescription Extraction | AI Chatbot Interface |
| :--- | :--- |
| ![Interface 2](interface2.png) | ![Interface 3](interface3.png) |
| *Processing OCR data* | *Context-aware health Q&A* |

---

### 📬 Contact & Support

**Developer:** Pragna Padamata  
**Email:** [pragnasrilalithapadamata@gmail.com](mailto:pragnasrilalithapadamata@gmail.com)  

---
### 📜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute!
