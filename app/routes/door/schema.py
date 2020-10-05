from pydantic import BaseModel


class Door(BaseModel):
    status: int = None