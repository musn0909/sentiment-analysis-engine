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