from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

class Confirmation(BaseModel):
    type: str
    group_id: int


app = FastAPI()

#
# @app.post("/conf")
# async def create_item(confirmation: Confirmation):
#     return '0fc10f4c'

@app.get("/conf", response_class=PlainTextResponse)
async def create_item():
    return '0fc10f4c'

