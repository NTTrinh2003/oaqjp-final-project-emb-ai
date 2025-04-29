"""
    This server contains only emotionDetector route
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods = ['GET'])
def emotion_detect():
    """
        Handle emotion detection route when a text is given
    """

    # Handle if the page was first initiated
    if not request.args:
        return render_template('index.html')
    # Get input
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Extract emotion
    emotions = emotion_detector(text_to_analyze)

    # Check if the text was valid
    if not emotions.get('dominant_emotion'):
        return "Invalid text! Please try again"
    # Create response message
    response = "For the given statement, the system response is "
    response += f"'anger': {emotions.get('anger')}, "
    response += f"'disgust': {emotions.get('disgust')}, "
    response += f"'fear': {emotions.get('fear')}, "
    response += f"'joy': {emotions.get('joy')}, "
    response += f"'sadness': {emotions.get('sadness')}. "
    response += f"The dominant emotion is {emotions.get('dominant_emotion')}"
    return response

if __name__ == "__main__":
    app.run(port=5001, debug=True)
