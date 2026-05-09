import os
import requests

# Detect Render deployment
IS_RENDER = os.getenv("RENDER") is not None


# =========================
# RENDER VERSION
# =========================
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

        try:

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=30
            )

            result = response.json()

            # Handle nested response
            prediction = result[0]

            if isinstance(prediction, list):
                prediction = prediction[0]

            return {
                "sentiment": prediction["label"],
                "confidence": round(prediction["score"], 4)
            }

        except Exception as e:

            return {
                "sentiment": "API ERROR",
                "confidence": 0,
                "details": str(e)
            }


# =========================
# LOCAL DEVELOPMENT VERSION
# =========================
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