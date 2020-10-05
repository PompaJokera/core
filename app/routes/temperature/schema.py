from pydantic import BaseModel


class Temperature(BaseModel):
    temperature: float = None
