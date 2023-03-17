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


@router.post("/", response_description="Add a new car")
async def create_car(request: Request, car: CarBase = Body(...)):
    car = jsonable_encoder(car)
    new_car = await request.app.mongodb["cars1"].find_one({"_id": new_car.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_car)
