"""
Emotion Detection Server
This script a Flask server for  detection based on user input .
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the input text for emotions and return the result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    return  (
            f" For the given statement, the system response is 'anger': {anger_score},"
            f" 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and"
            f" 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
    """
        This function renders the main application page 
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
