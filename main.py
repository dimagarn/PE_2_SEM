from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import json


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
labels = ["Visa invitation",
          "Visa extension",
          "Accommodation for international students",
          "Amount of people in a dormitory room",
          "Dormitory room readiness",
          "Dormitory the address",
          "Check in", "Other accomoation options",
          "Russian higher education system",
          "Point-Grade System",
          "Lectures begin and finish",
          "Not identified"]

with open('data.json', 'r') as file:
    answers = json.load(file)


@app.get("/")
async def root():
    return {'model': 'facebook/bart-large-mnli'}


@app.post("/predict/")
def predict(item: Item):
    """Text Classifier"""
    classified = classifier(item.text,
                            labels)["labels"][0]
    return answers[classified]
