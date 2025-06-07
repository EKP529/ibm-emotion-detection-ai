from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def use_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    detection = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is \
    'anger': {detection['anger']}, \
    'disgust': {detection['disgust']}, \
    'fear': {detection['fear']}, \
    'joy': {detection['joy']} and \
    'sadness': {detection['sadness']}. \
    The dominant emotion is {detection['dominant_emotion']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
