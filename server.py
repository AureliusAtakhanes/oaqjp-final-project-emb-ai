"""
Server module for the Emotion Detection application.
This module provides a Flask web interface that interacts with the
EmotionDetection package to analyze text sentiments.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the text provided in the request and returns the formatted response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None (indicating invalid input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment analysis results
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page (index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost at port 5000
    app.run(host="0.0.0.0", port=5000)
    