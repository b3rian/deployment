from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI() 
model = joblib.load('house_prediction.pkl') # loading the model

@app.get('/predict_price/')
async def predict_price(bedrooms : int, bathrooms: int, sqft : int):
    features = pd.DataFrame([[bedrooms, bathrooms, sqft]],
                            columns=["bedrooms", "bathrooms", "sqft"])
    price = model.predict(features)[0]
    return{'predicted price' : price}


 
