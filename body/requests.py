from pydantic import BaseModel


class TempBody(BaseModel):
    temp: float
