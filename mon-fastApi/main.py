from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, world!"}

class Item(BaseModel):
    name:str
    price:float
    
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": f"Item {item.name} with price {item.price} created"
    }


