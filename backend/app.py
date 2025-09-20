from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create an upload folder
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

    # Mock AI prediction (replace with your actual model code)
    prediction = {
        'filename': filename,
        'relevance_score': 87,  # Mock score
        'comments': 'This resume matches well with the job description.'
    }

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
