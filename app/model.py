from transformers import pipeline

# Load pretrained sentiment analysis model
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):

    result = classifier(text)

    return {
        "sentiment": result[0]["label"],
        "confidence": round(result[0]["score"], 4)
    }