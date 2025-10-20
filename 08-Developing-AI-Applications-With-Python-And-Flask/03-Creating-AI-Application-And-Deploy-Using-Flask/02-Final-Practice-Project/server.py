"""Flask web server for the Emotion Detection project.

Exposes a web interface and an API endpoint that analyze emotions in a
given text using the `emotion_detector` function from the package.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detection_route():
    """Handle GET requests for emotion detection.

    Reads the 'textToAnalyze' query parameter, calls the model, and
    returns a formatted, human-readable response. For invalid input,
    a friendly error message is returned.
    """
    text_to_analyze = (request.args.get("textToAnalyze") or "").strip()
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        # Handles invalid or blank input cases
        return "Invalid text! Please try again!", 200

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_response


@app.route("/")
def render_index_page():
    """Render the main index.html page for the web application."""
    return render_template("index.html")


def main():
    """Run the Flask web app on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
