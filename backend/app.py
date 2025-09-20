from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "GenAI Resume Backend is live!"

@app.route('/predict', methods=['POST'])
def predict():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = file.filename

    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # MOCK AI Prediction (replace this with your real AI model code)
    prediction = {
        'filename': filename,
        'relevance_score': 87,  # mock score
        'comments': 'This resume matches well with the job description.'
    }

    return jsonify(prediction)

if __name__ == "__main__":
    # Use Render's PORT environment variable if available
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
