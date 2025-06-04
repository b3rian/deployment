from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel, Field
import numpy as np

app = FastAPI() 
model = joblib.load('model.pkl') # loading the trained model

class InputData(BaseModel):
    sepal_length: float = Field(..., gt = 0, example = 2.1)
    sepal_width: float = Field(..., gt = 0, example = 5.1)
    petal_length: float = Field(..., gt = 0, examples=3.0)
    petal_length: float = Field(..., gt = 0)

@app.post('/predict/')
async def predict(data : InputData):
    input_array = np.array([[data.sepal_length, data.sepal_width,
                             data.petal_length, data.petal_width]])
    prediction = model.predict(input_array)[0]
    return {'prediction' : int(prediction)}

 


 
