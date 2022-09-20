# run from: uvicorn app.main:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Fast API World!!"}
