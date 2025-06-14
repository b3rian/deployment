from fastapi import FastAPI, HTTPException
from models import WeatherRequest, WeatherResponse
from weather_service import get_weather

# FastAPI application setup
app = FastAPI(title="Weather Forecast API")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Weather Forecast API!"}

@app.post("/weather", response_model=WeatherResponse)
async def fetch_weather(request: WeatherRequest):
    weather = await get_weather(request.city)
    if "error" in weather:
        raise HTTPException(status_code=404, detail=weather["error"])
    return weather
