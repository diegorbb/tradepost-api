from fastapi import FastAPI
from . import models
from .database import engine

# This line tells SQLAlchemy to create all the tables based on our models
# It checks if the table exists first, so it won't try to recreate it on every run
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TradePost API! Now with a database!"}