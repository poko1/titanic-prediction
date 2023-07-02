from fastapi import FastAPI
from joblib import load
import joblib

classifier = joblib.load('survival_pred.pkl')

def classify(classifier, pclass, sex, fare):
    passenger_prediction = classifier.predict([[pclass, sex, fare]])
    res = 'Did Not Survive' if passenger_prediction == 0 else 'Survived'
    return {'label': res}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Welcome to the Classic Titanic Survival Prediction API'}

@app.post('/tinatic_prediction')
def tinatic_prediction(pclass: int, sex: int, fare: float):
    return classify(classifier, pclass, sex, fare)