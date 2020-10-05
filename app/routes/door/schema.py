import string
from typing import

from pydantic import BaseModel


class Humidity(BaseModel):
    humidity: float = None
    envioronment: str = None