from fastapi import FastAPI
import json, os
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from fastapi.testclient import TestClient

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

