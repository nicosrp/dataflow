from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return jsonify({"message": "No file uploaded"}), 400
    
    # Example: Read the file content (modify this based on what you need)
    file_content = file.read().decode('utf-8')
    
    # Process file (e.g., count words in the text)
    word_count = len(file_content.split())

    return jsonify({"message": f"File processed! Word count: {word_count}"})

if __name__ == '__main__':
    app.run(debug=True)