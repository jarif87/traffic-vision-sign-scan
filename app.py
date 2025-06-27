from flask import Flask, render_template, request, Response, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define class names
class_names = {
    0: "Green Light",
    1: "Red Light",
    2: "Speed Limit 10",
    3: "Speed Limit 100",
    4: "Speed Limit 110",
    5: "Speed Limit 120",
    6: "Speed Limit 20",
    7: "Speed Limit 30",
    8: "Speed Limit 40",
    9: "Speed Limit 50",
    10: "Speed Limit 60",
    11: "Speed Limit 70",
    12: "Speed Limit 80",
    13: "Speed Limit 90",
    14: "Stop"
}

# Load YOLO model
model = YOLO("model/best.pt")

# Set up upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed video extensions
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Generate frames for real-time detection
def gen_frames():
    cap = cv2.VideoCapture(0)  # Use webcam (0) for real-time feed
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Perform YOLO detection
            results = model(frame)
            annotated_frame = results[0].plot()  # Draw bounding boxes and labels

            # Encode frame as JPEG
            ret, buffer = cv2.imencode(".jpg", annotated_frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    cap.release()

# Process uploaded video
def process_video(filepath):
    cap = cv2.VideoCapture(filepath)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Perform YOLO detection
            results = model(frame)
            annotated_frame = results[0].plot()

            # Encode frame as JPEG
            ret, buffer = cv2.imencode(".jpg", annotated_frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    cap.release()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        return jsonify({"filename": filename}), 200
    return jsonify({"error": "Invalid file format"}), 400

@app.route("/process_video/<filename>")
def process_video_feed(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    return Response(process_video(filepath), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)