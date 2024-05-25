from fastapi.testclient import TestClient
from app.main import app
import json


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'model': 'facebook/bart-large-mnli'}


def test_predict_answer():
    response = client.post("/predict/",
                           json={"text": "I applied for a visa invitation "
                                 "a few days/weeks ago and still haven't "
                                 "received it. What should I do in "
                                 "this situation?"})
    assert response.status_code == 200
    assert response.json() == json.load(open('data/data.json',
                                             'r',
                                             encoding='utf-8'))['Visa invitation']


def test_wrong_question():
    response = client.post("/predict/",
                           json={"text": "I love cats!"})
    assert response.status_code == 200
    assert response.json() == json.load(open('data/data.json',
                                             'r',
                                             encoding='utf-8'))['"Not identified']


def test_health():
    response = client.post("/health/")
    assert response.status_code == 200
    assert response == "Yes"
