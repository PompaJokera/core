from fastapi import APIRouter, Depends
from app.routes.temperature.schema import Temperature

router = APIRouter()


@router.post("/temperature", response_model=Temperature)
async def add_temperature():
    print("dodaje temperature")


@router.get("/temperature", response_model=Temperature)
async def get_temperature():
    print("pobieram temperature")
    temp = 25.4
    return "temperature", temp
