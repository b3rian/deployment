from fastapi import FastAPI, Cookie, Header, HttpException, status, Request
import pandas as pd
import joblib
import time
from pydantic import BaseModel, Field
import numpy as np
from typing import Annotated, Optional

app = FastAPI() # App instance
model = joblib.load('model.pkl') # loading the trained model

@app.middleware('http')
async def log_and_time_requests(request: Request, call_next):
    start_time = time.time()
    print(f"Received request at: {request.url}")
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    print(f"Processed in {duration:.4f} seconds")
    
    return response

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

@app.post("/predict", response_model=PredictionResponse, status_code = status.HTTP_201_CREATED)
async def predict(data : InputData):
  try:
    # Convert input data to a numpy array for prediction
    input_array = np.array([[data.feature_1, data.feature_2, data.feature_3, data.feature_4]])
    prediction = model.predict(input_array)[0]
    confidence = model.predict_proba(input_array).max()
    return PredictionResponse(prediction=prediction, confidence=confidence)

  except ValueError as e:
    raise HttpException(status_code = 400, detail = str(e))
  
  except Exception as e:
    raise HttpException(status_code=500, detail = 'Internal Server Error')


 


 
