from typing import List

from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from config import TOKEN_VK, TOKEN_CONF_VK
from datetime import datetime
from fastapi.responses import PlainTextResponse


class Confirmation(BaseModel):
    type: str
    group_id: int


class Photo(BaseModel):
    id: str
    type: str
    photo_130: str
    photo_604: str


class Video(BaseModel):
    id: str
    title: str
    description: str
    duration: int
    player: str


class Attachment(BaseModel):
    type: str
    photo: Photo


class Post(BaseModel):
    id: str
    date: datetime
    text: str
    attachments: List[Attachment]


class Event(BaseModel):
    type: str = ''
    event_id: str = ''
    v: float = 0
    group_id: str = ''
    object: Post = None


app = FastAPI()


@app.post("/")
async def vk_handler(req: Request):
    try:
        data = await req.json()
    except Exception:
        print("Empty request")
        return Response("not today", status_code=403)

    if data["type"] == "confirmation":
        print("Send confirmation token: {}", TOKEN_CONF_VK)
        return Response(TOKEN_CONF_VK)

    if data["type"] == 'wall_post_new':
        print(data)
        return Response('ok')
    return Response("ok")