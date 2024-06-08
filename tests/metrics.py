from app.main import app
from fastapi.testclient import TestClient
import pandas as pd
from sklearn.metrics import accuracy_score
import json

client = TestClient(app)

df = pd.read_csv("data/questions_and_descriptions.csv")

true_answers = []
predictions = []

data = json.load(open('data/data.json', 'r', encoding='utf-8'))

for index, row in df.iterrows():
    question = row["Questions"]
    true_answer_label = row["Description"]

    response = client.post("/predict/", json={"text": question})

    if response.status_code == 200:
        answer = response.json()

        true_answers.append(data[true_answer_label])
        predictions.append(answer)
    else:
        print(f"Failed to get a response for question: {question}")

accuracy = accuracy_score(true_answers, predictions)
print(f"Accuracy: {accuracy}")
