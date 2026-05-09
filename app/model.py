from textblob import TextBlob


def analyze_sentiment(text: str):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "POSITIVE"

    elif polarity < 0:
        sentiment = "NEGATIVE"

    else:
        sentiment = "NEUTRAL"

    return {
        "sentiment": sentiment,
        "confidence": round(abs(polarity), 4)
    }