
# Personalized Compliment Generator

![Emotion Detector Banner](https://www.retorio.com/hubfs/Retorio%20What%20is%20the%20difference%20between%20facial%20expression%20detection%20and%20recognition_.webp)  
*Detect and generate compliments based on facial emotions.*

This project uses OpenCV for facial detection, the FER (Facial Emotion Recognition) library for emotion recognition, and a custom text-to-speech (TTS) system to provide compliments based on detected facial expressions. It aims to detect emotions from an image or video, generate a related compliment, and speak the compliment aloud using a TTS engine.

## Features

- **Facial Detection**: Detects faces using Haar Cascade Classifier.
- **Emotion Recognition**: Identifies emotions such as happiness, sadness, anger, surprise, fear, and others using FER.
- **Compliment Generation**: Generates and speaks personalized compliments based on the detected emotion.
- **Real-Time Interaction**: Allows emotion detection in both images and live video streams.
- **Text-to-Speech**: Converts generated compliments into speech.

## Requirements

- Python 3.x
- OpenCV
- FER (Facial Expression Recognition) library
- pyttsx3 (for text-to-speech functionality)
- numpy
- threading (for handling background speech processing)
- queue

## Setting Up a Virtual Environment

To ensure that the project dependencies do not interfere with other Python projects, it is recommended to use a virtual environment.

### Steps to Create a Virtual Environment:

1. **Install `virtualenv` (if not installed)**:
    If you don't have `virtualenv` installed, run the following command:

    ```bash
    pip install virtualenv
    ```

2. **Create a Virtual Environment**:
    Navigate to your project folder and create a new virtual environment by running:

    ```bash
    python -m venv venv
    ```

    This will create a folder named `venv` in your project directory, which will contain the virtual environment.

3. **Activate the Virtual Environment**:

    - On **Windows**:

    ```bash
    .\\venv\\Scripts\\activate
    ```

    - On **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

    You should see the virtual environment's name (e.g., `(venv)`) appear in your terminal prompt, indicating that the virtual environment is active.

4. **Install the Required Dependencies**:
    Now, with the virtual environment activated, install the dependencies required for this project:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file yet, you can manually install the dependencies with:

    ```bash
    pip install opencv-python fer pyttsx3 numpy
    ```

5. **Deactivating the Virtual Environment**:
    When you're done working in the virtual environment, you can deactivate it by running:

    ```bash
    deactivate
    ```

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Naren456/Personalized-Compliment-Generator.git
    ```

2. **Create and Activate a Virtual Environment**:
    Follow the steps above to create and activate the virtual environment.

3. **Install Dependencies**:
    With the virtual environment activated, install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Emotion Detection in Image**: Detect emotion from an image.
    ```bash
    python main.py
    ```
    - Choose option 1 from the menu.
    - Provide the path to the image file.

2. **Emotion Detection in Video**: Detect emotion from a video file.
    ```bash
    python main.py
    ```
    - Choose option 2 from the menu.
    - Provide the path to the video file.

3. **Real-Time Emotion Detection**: Start a webcam session to detect emotions in real time.
    ```bash
    python main.py
    ```
    - Choose option 3 from the menu.

4. **Exit**: To exit the program, simply choose option 4.

## Demo Video

To get a better understanding of how the Emotion Detector with Compliment Generator works, you can watch the demo video below:

[![Emotion Detector Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://youtu.be/e9rwDUICb0E)

In this demo, you will see how the program detects emotions from a live video feed and generates compliments based on the detected emotions.

## How It Works

- **Face Detection**: OpenCV detects faces in images and video streams using Haar Cascade Classifier.
- **Emotion Recognition**: FER library recognizes emotions based on the facial expressions of the detected faces.
- **Compliment Generation**: Depending on the recognized emotion, a corresponding compliment is generated.
- **Text-to-Speech**: The compliment is spoken out loud using the pyttsx3 library.

## Code Overview

### `Emotion_Detector`
- Initializes face detection and emotion detection systems.
- Detects emotions from images or video frames and generates a compliment.
- Speaks the compliment using the `TextToSpeech` class.

### `Compliment`
- Stores predefined compliments based on various emotions.
- Returns a compliment based on the detected emotion.

### `TextToSpeech`
- Handles text-to-speech functionality in a separate thread to ensure non-blocking speech.
- Uses pyttsx3 to convert text into speech.

## Example Compliments

- **Happy**: \"You're doing great! Keep smiling!\"
- **Sad**: \"It's okay to feel down sometimes, but you'll get through this.\"
- **Angry**: \"Take a deep breath, you're stronger than you think.\"
- **Surprised**: \"Wow! That was unexpected, but you're handling it well!\"
- **Neutral**: \"You're calm and collected, stay positive!\"
- **Fear**: \"You're brave for facing your fears, keep going!\"

## Challenges Faced

### Problem with `pyttsx3`:
Initially, the program experienced freezing frames when speaking compliments. This occurred because the `pyttsx3` library ran on the main thread, blocking other processes like video frame updates.

### Solution: Using Threading
To fix this, threading was implemented to run the text-to-speech (TTS) functionality in a separate thread. This ensured smooth and uninterrupted video processing while compliments were spoken.

### Why Threading Was Used:
- Prevented the main thread from being blocked.
- Maintained real-time performance and interaction.
- Allowed for a seamless user experience.

### How Threading Helped:
- TTS ran independently of the video processing.
- Improved performance and responsiveness of the application.
- Enabled scalability for future enhancements.

## Acknowledgments

- [OpenCV](https://opencv.org/) for face detection.
- [FER](https://github.com/priya-dwivedi/fer) for emotion recognition.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech functionality.""
