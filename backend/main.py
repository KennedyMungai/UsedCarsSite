"""The main script for the backend"""
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os

ENV = find_dotenv(load_dotenv())


DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]
    

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()