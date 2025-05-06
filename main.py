from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field, Query, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str = Field(..., max_length=50, examples=["Item1", "Item2"])
    description: str | None = Field(None, max_length=100, 
           description="A short description of the item", examples=["A nice item", "An awesome item"])
    price: float
    tax: float | None = Field(None, gt=0)
    tags: set[str] = Field(default_factory=set, 
           description="A list of tags associated with the item")
    image: Image | None = None

class User(BaseModel):
    id: int
    name: str
    email: str

@app.put(/"items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    user: Annotated[User, Query(description="The user who is updating the item")],
    q: str | None = Query(None, max_length=50)
):
    return {"item_id": item_id, "item": item, "user": user, "q": q}
