from fastapi import FastAPI
from app.models import Item
from app.text_classifier import text_classifier


app = FastAPI()


@app.get("/")
async def root():
    return {'model': 'facebook/bart-large-mnli'}


@app.post("/predict/")
def predict(item: Item):
    """Text Classifier"""
    prediction = text_classifier.predict(item.text)
    return prediction


@app.post("/health/")
def health():
    return "Yes"
