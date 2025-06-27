# traffic sign ai detector

A Flask-based web application for detecting traffic signs in real-time using a webcam or uploaded videos. The application leverages a YOLO model (`best.pt`) to identify traffic signs, such as "Stop," "Green Light," and various speed limits, with a modern, user-friendly interface featuring a YouTube-like video player. Built by Sadik Al Jarif.

![Wbpage Screenshot](/images/image.png/)

## Features

- **Real-Time Detection**: Detects traffic signs in live webcam feed with a toggleable on/off button.
- **Video Upload**: Upload MP4, AVI, or MOV videos for traffic sign detection, displayed with a sleek video player.
- **Modern UI**: Compact, eye-catching design with gradient styling, animations, and responsive layout.
- **YouTube-Like Controls**: Video player with professional controls for uploaded videos.
- **Supported Signs**: Recognizes 15 traffic sign classes, including:
  - Green Light, Red Light, Stop
  - Speed Limits (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

## Prerequisites

- Python 3.8+
- A webcam for real-time detection
- A trained YOLO model (`best.pt`) placed in the `model/` folder
- Git (for cloning the repository)

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/<your-username>/traffic-sign-ai-detector.git
   cd traffic-sign-ai-detector

   ```
2. **Set Up a Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies:**
```
pip install flask opencv-python ultralytics numpy werkzeug
```

- Place the YOLO Model:
    - Ensure the trained model file best.pt is in the model/ folder. If you don’t have the model, contact the repository owner or train a YOLO model with the 15 traffic sign classes.

4. **Create the Uploads Folder:**
```
mkdir uploads
touch uploads/.gitkeep
```

### Usage

5. **Run the Application:**
```

python app.py

```

- Real-Time Webcam Detection:
    - Open the app in a browser.

    - Click "Open Camera" to start the webcam feed with traffic sign detection.

    - Click "Close Camera" to stop the feed.

- Video Upload Detection:
    - In the "Upload Video for Detection" section, select an MP4, AVI, or MOV file.

    - Click "Upload Video" to process and display the video with detected signs.

    - Use the video player controls to play, pause, or seek through the processed video.

### File Structure

```
traffic-sign-ai-detector/
├── model/
│   └── best.pt              # YOLO model file (excluded from git)
├── static/
│   └── style.css            # Styling for the web interface
├── templates/
│   └── index.html           # HTML template for the UI
├── uploads/
│   └── .gitkeep             # Placeholder to keep uploads folder in git
├── app.py                   # Main Flask application
├── .gitignore               # Git ignore file
└── README.md                # Project documentation
```

### Notes


- Performance: Real-time detection performance depends on your hardware. A GPU with CUDA support is recommended for faster inference.

- Browser Compatibility: Tested on Chrome, Firefox, and Edge. Ensure camera permissions are enabled for webcam access.

- Responsive Design: The UI is optimized for desktop and mobile devices.

