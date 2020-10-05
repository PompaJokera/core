import string

from pydantic import BaseModel


class Humidity(BaseModel):
    humidity: float = None
    envioronment: str = None