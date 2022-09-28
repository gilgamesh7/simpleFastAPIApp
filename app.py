from fastapi import FastAPI

from model import Developer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "In God We Trust!"}

@app.post("/")
async def create_developer(developer: Developer):
    return developer
