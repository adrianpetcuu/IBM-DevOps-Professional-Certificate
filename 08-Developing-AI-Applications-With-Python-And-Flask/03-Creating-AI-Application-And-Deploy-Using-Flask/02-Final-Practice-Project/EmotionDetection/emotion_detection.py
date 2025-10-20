"""Emotion detection module using IBM Watson NLP Emotion Predict API."""

import requests
import json


def emotion_detector(text_to_analyze):
    """Send the input text to Watson NLP Emotion API and return emotion scores.

    Args:
        text_to_analyze (str): The text whose emotions need to be analyzed.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    if not text_to_analyze.strip():
        # Handle blank input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response_data = json.loads(response.text)
    emotions = response_data.get("emotionPredictions", [])[0]["emotion"]

    anger_score = emotions.get("anger")
    disgust_score = emotions.get("disgust")
    fear_score = emotions.get("fear")
    joy_score = emotions.get("joy")
    sadness_score = emotions.get("sadness")

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
