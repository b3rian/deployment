from pydantic import BaseModel, Field
 

# Api request model
class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    description: str
    temperature: float
    feels_like: float
    humidity: int

 


 


 
