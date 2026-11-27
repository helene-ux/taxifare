from fastapi import FastAPI
import pandas as pd
from taxifare.predict import load_model, predict as model_predict
app = FastAPI()

model = load_model("models/linreg_pipeline.joblib")

@app.get("/")
def root():
    return {"message": "Welcome to TaxiFare API"}

@app.get("/predict")
def predict(
    pickup_datetime: str,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int
):
    data = pd.DataFrame([{
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }])

    prediction = model_predict(model, data)

    return {"fare": float(prediction[0])}
