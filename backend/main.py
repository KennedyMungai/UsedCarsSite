"""The main script for the backend"""
import os

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from uvicorn import run
from routers.cars import router as cars_router


ENV = find_dotenv(load_dotenv())


DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

app = FastAPI()

app.include_router(cars_router, prefix="/cars", tags=["cars"])


@ app.on_event("startup")
async def startup_db_client():
    """The database connection code"""
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]


@ app.on_event("shutdown")
async def shutdown_db_client():
    """The database disconnection code"""
    app.mongodb_client.close()


if __name__ == "__main__":
    run("main:app", reload=True)
