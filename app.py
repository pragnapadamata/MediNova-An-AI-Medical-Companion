from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama
from flask import Flask, request, jsonify, render_template
import pandas as pd
from rapidfuzz import fuzz, process
import pytesseract
from PIL import Image
import io
import google.generativeai as genai

# 👉 Configure Gemini API Key
genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxx")  # replace with your actual key

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Load medicine data
medicine_df = pd.read_csv('Medicine_Details.csv')
medicine_names = medicine_df['Medicine Name'].tolist()

# 🔍 Prepare RAG embedding index
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

medicine_df["full_text"] = medicine_df.apply(lambda row: f"""
Medicine: {row['Medicine Name']}
Uses: {row.get('Uses', 'N/A')}
Side Effects: {row.get('Side_effects', 'N/A')}
Composition: {row.get('Composition', 'N/A')}
""", axis=1)

embeddings = embed_model.encode(medicine_df["full_text"].tolist()).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# 🌐 Gemini general reply
def get_general_reply_from_gemini(user_input):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return "Hey there! 👋 Feel free to ask me anything about medicines."

# 🧠 Mistral RAG answer
def smart_medicine_answer(user_query, k=3):
    query_embedding = embed_model.encode([user_query])[0].astype("float32")
    _, indices = index.search(np.array([query_embedding]), k)
    relevant_rows = medicine_df.iloc[indices[0]]["full_text"].tolist()

    context = "\n\n".join(relevant_rows)
    prompt = f"""
You are a helpful AI doctor. Based on the following medicine information, answer the user's question.

Medicine Data:
{context}

User Question: {user_query}

Answer in simple language:
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

# 🔎 Fuzzy medicine detail search
def get_medicine_details(name_query):
    formatted_query = name_query.title()
    match_result = process.extractOne(formatted_query, medicine_names, scorer=fuzz.WRatio)
    if match_result:
        best_match = match_result[0]
        matched_row = medicine_df[medicine_df['Medicine Name'] == best_match].iloc[0]
        reply = f"Medicine: {matched_row['Medicine Name'].strip()}\n"
        reply += f"Uses: {matched_row.get('Uses', 'No data').strip()}\n"
        reply += f"Side Effects: {matched_row.get('Side_effects', 'No data').strip()}\n"
        reply += f"Composition: {matched_row.get('Composition', 'No data').strip()}"
        return reply
    else:
        return "No matching medicine found."

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files.get('image')
        if not image:
            return render_template('upload_image.html', response=None, extracted="No image uploaded.")
        
        img = Image.open(io.BytesIO(image.read()))
        extracted_text = pytesseract.image_to_string(img)
        formatted_text = extracted_text.title()

        match_result = process.extractOne(formatted_text, medicine_names, scorer=fuzz.WRatio)
        if match_result:
            best_match = match_result[0]
            structured_data = get_medicine_details(best_match)

            if structured_data:
                return render_template('upload_image.html', response=structured_data, extracted=formatted_text)
        
        return render_template('upload_image.html', response=None, extracted=formatted_text)

    return render_template('upload_image.html', response=None)

# 💬 Main message route with Gemini fallback
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').strip().lower()
    if not user_message:
        return jsonify({'response': "Please enter a valid message."})

    # 🚨 Handle greetings or general convo with Gemini
    GREETINGS = ['hi', 'hello', 'hey', 'how are you', 'hlo', 'hola', 'yo', 'sup', 'what’s up']
    if any(greet in user_message for greet in GREETINGS):
        reply = get_general_reply_from_gemini(user_message)
        return jsonify({'response': reply})

    # 🧠 Default to RAG-based Mistral
    reply = smart_medicine_answer(user_message)
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
