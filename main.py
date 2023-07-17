from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Query
from typing import Annotated


class Confirmation(BaseModel):
    type: str
    group_id: int


app = FastAPI()


@app.post("/conf")
async def create_item(confirmation: Confirmation):
    return '0fc10f4c'

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
