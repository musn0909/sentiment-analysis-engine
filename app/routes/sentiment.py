from fastapi import APIRouter
from app.schemas import TextInput
from app.model import analyze_sentiment

router = APIRouter()

@router.post("/predict")
def predict_sentiment(data: TextInput):

    result = analyze_sentiment(data.text)

    return result