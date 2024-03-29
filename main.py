from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name=str
    price:float
    is_offer:Union[bool,None]=None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/nona")
def hola_root():
    return {"Hello": "nona"}



@app.get("/items/{item_id}")
def read_items(item_id:int,q:Union[str,None]=None):
    return {"item_id": item_id,'q':q}
