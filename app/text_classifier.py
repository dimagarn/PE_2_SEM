from transformers import pipeline
import json


class TextClassifier:
    def __init__(self, model_name, labels, answers_file):
        self.classifier = pipeline("zero-shot-classification", model=model_name)
        self.labels = labels
        with open(answers_file, 'r') as file:
            self.answers = json.load(file)

    def predict(self, text):
        if self.classifier(text, self.labels)["scores"][0] < 0.25:
            return self.answers["Not identified"]
        classified_label = self.classifier(text, self.labels)["labels"][0]
        return self.answers[classified_label]


labels = ["Visa invitation",
          "Visa extension",
          "Accommodation for international students",
          "Amount of people in a dormitory room",
          "Dormitory room readiness",
          "Dormitory address",
          "Check in", "Other accommodation options",
          "Russian higher education system",
          "Point-Grade System",
          "Lectures begin and finish",
          "Not identified"]

text_classifier = TextClassifier(model_name="facebook/bart-large-mnli",
                                 labels=labels,
                                 answers_file='data/data.json')
