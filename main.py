from pydantic import BaseModel, Field
 
class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    description: str
    temperature: float
    feels_like: float
    humidity: int

 


 


 
