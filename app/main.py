import requests
import os

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

    return {
        "sentiment": result[0][0]["label"],
        "confidence": round(result[0][0]["score"], 4)
    }