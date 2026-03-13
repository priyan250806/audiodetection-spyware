from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "recordings"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    audio = request.files['audio']
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".webm"
    path = os.path.join(UPLOAD_FOLDER, filename)
    audio.save(path)
    return "saved"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
