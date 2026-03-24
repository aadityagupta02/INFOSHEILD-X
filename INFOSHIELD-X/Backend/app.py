from flask import Flask, request, jsonify
from flask_cors import CORS
from services.text_service import analyze_text
from services.image_service import analyze_image
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "INFOSHIELD-X backend is running 🚀"


@app.route("/detect-text", methods=["POST"])
def detect_text():
    data = request.get_json(silent=True)

    if not data or "text" not in data:
        return jsonify({
            "error": "No text provided"
        }), 400

    text = data["text"].lower()

    response = analyze_text(text)

    return jsonify({
        "input_text": text,
        "result": response["result"],
        "confidence_percent": response["confidence_percent"]
    })
@app.route("/detect-image", methods=["POST"])
def detect_image():
    if "image" not in request.files:
        return jsonify({
            "error": "No image file provided"
        }), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({
            "error": "Empty filename"
        }), 400

    file_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(file_path)

    response = analyze_image(file_path)

    return jsonify({
        "filename": image.filename,
        "result": response["result"],
        "confidence_percent": response["confidence_percent"]
    })




if __name__ == "__main__":
    app.run(debug=True)
