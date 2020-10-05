from pydantic import BaseModel


class Relay(BaseModel):
    status: int = None
