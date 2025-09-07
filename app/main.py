from fastapi import FastAPI
from .routers import users 

app = FastAPI()

app.include_router(users.router) # <-- INCLUDE THE ROUTER IN THE APP

@app.get("/")
def read_root():
    return {"message": "Welcome to the TradePost API!"}