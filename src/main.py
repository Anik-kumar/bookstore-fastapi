"""The typing module: Support for gradual typing as defined by PEP"""
import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """This is a test route which returns a dictionary."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """This is a test route which returns item details."""
    return {"item_id": item_id, "quantity": random.randint(100, 1001)}
