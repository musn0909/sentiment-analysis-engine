import os
import requests

# Check if running on Render
IS_RENDER = os.getenv("RENDER") is not None


if IS_RENDER:

    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

    HF_TOKEN = os.getenv("HF_TOKEN")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    def analyze_sentiment(text: str):

        payload = {
            "inputs": text
        }

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        result = response.json()

        prediction = result[0]

        if isinstance(prediction, list):
            prediction = prediction[0]

        return {
            "sentiment": prediction["label"],
            "confidence": round(prediction["score"], 4)
        }

else:

    from transformers import pipeline

    classifier = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    def analyze_sentiment(text: str):

        result = classifier(text)

        return {
            "sentiment": result[0]["label"],
            "confidence": round(result[0]["score"], 4)
        }