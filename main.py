from fastapi import FastAPI, Cookie, Header, HttpException, status, Request, BackgroundTasks
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import time
from typing import Annotated, Optional

app = FastAPI()

from pydantic import BaseModel

# models with pydantic
class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    description: str
    temperature: float
    feels_like: float
    humidity: int

 


 


 
