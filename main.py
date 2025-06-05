from fastapi import FastAPI, Cookie, Header, HttpException
import pandas as pd
import joblib
from pydantic import BaseModel, Field
import numpy as np
from typing import Annotated, Optional

app = FastAPI() 
model = joblib.load('model.pkl') # loading the trained model

# Define the request model
class InputData(BaseModel):
    feature_1: float = Field (..., description="Sepal Length")
    feature_2: float = Field(..., description="Sepal Width")
    feature_3: float = Field(..., description="Petal Length")
    feature_4: float = Field(..., description="Petal Width")
     
# Define the response model
class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="Predicted class label")
    confidence: float = Field(..., description="Confidence score of the prediction")

@app.post("/predict", response_model=PredictionResponse)
async def predict(data : InputData):
  try:
    # Convert input data to a numpy array for prediction
    input_array = np.array([[data.feature_1, data.feature_2, data.feature_3, data.feature_4]])
    prediction = model.predict(input_array)[0]
    confidence = model.predict_proba(input_array).max()
    return PredictionResponse(prediction=prediction, confidence=confidence)

  except Exception as e:
    raise HttpException(status_code=500, detail=str(e))


 


 
