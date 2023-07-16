"""The typing module: Support for gradual typing as defined by PEP"""
import random

from fastapi import FastAPI, Depends
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from . import models, schemas


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def home():
    """This is a test route which returns a dictionary."""
    return {"Hello": "World"}


@app.post('/item')
def create(item: models.Item, db: Session = Depends(connect_db)):
    new_item = models.Item(name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh()
    return new_item


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """This is a test route which returns item details."""
    return {"item_id": item_id, "quantity": random.randint(100, 1001)}
