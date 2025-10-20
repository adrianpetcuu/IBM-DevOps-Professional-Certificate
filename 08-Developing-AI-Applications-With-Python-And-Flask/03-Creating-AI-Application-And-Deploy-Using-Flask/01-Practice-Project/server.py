"""This module runs a Flask web app that performs sentiment analysis.
It provides routes for text analysis and a simple web interface.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Analyze the sentiment of a given text provided as a query parameter."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."

    sentiment_type = label.split('_')[1]
    return f"The given text has been identified as {sentiment_type} with a score of {score}."


@app.route("/")
def render_index_page():
    """Render the main index page for the Flask app."""
    return render_template('index.html')


if __name__ == "__main__":
    # Run the Flask app and expose it on localhost:5000.
    app.run(host="0.0.0.0", port=5000)
