from fastapi import APIRouter, Depends
from app.routes.relay.schema import Relay

router = APIRouter()


@router.post("/{id}", response_model=Relay)
async def action():
    return {id: id}


@router.get("/{id}")
async def get_status():
    return {id: str(id)}
