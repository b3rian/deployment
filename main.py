from fastapi import FastAPI, Cookie, Header, HttpException, status, Request, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Annotated, Optional
import httpx
import os
from dotenv import load_dotenv

app = FastAPI()

from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    description: str
    temperature: float
    feels_like: float
    humidity: int

 


 


 
