"""The file that holds the logic for the cars route"""
from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import CarBase

router = APIRouter()


@router.get("/", response_description="List all cars")
async def list_cars() -> dict:
    """Amn api endpoint for getting the cars

    Returns:
        dict: A message to show the proper running of the code
    """
    return {"data": "All cars will go here"}
