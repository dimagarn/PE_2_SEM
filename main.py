from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import json

class Item(BaseModel):
    text: str

class TextClassifier:
    def __init__(self, model_name, labels, answers_file):
        self.classifier = pipeline("zero-shot-classification", model=model_name)
        self.labels = labels
        with open(answers_file, 'r') as file:
            self.answers = json.load(file)

    def predict(self, text):
        classified_label = self.classifier(text, self.labels)["labels"][0]
        return self.answers[classified_label]

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

text_classifier = TextClassifier(model_name="facebook/bart-large-mnli",
                                 labels=labels,
                                 answers_file='data.json')

app = FastAPI()

@app.get("/")
async def root():
    return {'model': 'facebook/bart-large-mnli'}

@app.post("/predict/")
def predict(item: Item):
    """Text Classifier"""
    prediction = text_classifier.predict(item.text)
    return prediction
