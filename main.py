from fastapi import FastAPI

from db import create_tables

app = FastAPI()


@app.get("/db")
async def root():
    await create_tables()
    return {"msg": "ok"}
