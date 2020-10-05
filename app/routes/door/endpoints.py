from fastapi import APIRouter
from app.routes.door.schema import Door
import logging
from fastapi.logger import logger
router = APIRouter()


@router.post("/door", response_model=Door)
async def add_door_status():
    print("dodaje drzwi")


@router.get("/door ", response_model=Door)
async def get_status():
    print("pobieram status drzwi")
