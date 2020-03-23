#! /usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from orm import db_connection, create_tables
from orm.tables import test
import socket
import time
import uvicorn
import json
from body.requests import TempBody

app = FastAPI()


def parse_json(request):
    return json.loads(str(request.json).replace("'", '"'))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


@app.post("/test", status_code=200)
def testpost(temp: TempBody):
    tempetarure = temp.temp
    test.add_temp(tempetarure)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
