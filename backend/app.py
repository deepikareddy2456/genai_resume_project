from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder to store uploaded PDFs
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "GenAI Resume Backend is live!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # MOCK prediction (replace with AI logic if needed)
    prediction = {
        'filename': filename,
        'relevance_score': 87,
        'comments': 'This resume matches well with the job description.'
    }

    return jsonify(prediction)

if __name__ == "__main__":
    # Render assigns the PORT environment variable dynamically
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
