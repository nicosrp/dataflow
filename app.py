import os
import fitz  # PyMuPDF (for PDFs)
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}  # Add more file types if needed

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400
    
    file = request.files['file']

    if not allowed_file(file.filename):
        return jsonify({"message": "Invalid file type. Only .txt and .pdf allowed"}), 400

    # **Handle TXT Files**
    if file.filename.endswith('.txt'):
        file_content = file.read().decode('utf-8')
        word_count = len(file_content.split())
        return jsonify({"message": f"TXT file processed! Word count: {word_count}"})

    # **Handle PDF Files**
    elif file.filename.endswith('.pdf'):
        doc = fitz.open(stream=file.read(), filetype="pdf")  # Open PDF
        text = "\n".join([page.get_text() for page in doc])  # Extract text
        word_count = len(text.split())
        return jsonify({"message": f"PDF file processed! Word count: {word_count}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
