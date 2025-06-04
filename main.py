from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel
import numpy as np

app = FastAPI() 
model = joblib.load('model.pkl') # loading the trained model

class InputData(BaseModel):
    age : int
    salary : float

@app.post('/predict')
async def predict(data : InputData):
    input_array = np.array([[data.age, data.salary]])
    prediction = model.predict(input_array)[0]
    return {'prediction' : int(prediction)}

 


 
