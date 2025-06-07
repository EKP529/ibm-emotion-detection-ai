''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def home():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def use_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using the emotion_detector()
        function. The output returned shows several emotions, their confidence 
        score, and the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    detection = emotion_detector(text_to_analyze)

    if detection['dominant_emotion'] is None:
        return 'Invalid text! Please try again.'

    return f"For the given statement, the system response is \
    'anger': {detection['anger']}, \
    'disgust': {detection['disgust']}, \
    'fear': {detection['fear']}, \
    'joy': {detection['joy']} and \
    'sadness': {detection['sadness']}. \
    The dominant emotion is {detection['dominant_emotion']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
