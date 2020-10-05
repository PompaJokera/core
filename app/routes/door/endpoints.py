from fastapi import APIRouter, Depends
from app.routes.humidity.schema import Humidity

router = APIRouter()


@router.post("/humidity", response_model=Humidity)
async def add_humidity():
    print("dodaje wilgotność")
