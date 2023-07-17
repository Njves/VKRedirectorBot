from typing import List

from fastapi import FastAPI, Request
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
    small_photo: str
    big_photo: str


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
async def create_item(event: Event):
    if event.type == 'confirmation':
        return PlainTextResponse(TOKEN_CONF_VK)
    if event.type == 'wall_post_new':
        print(event.object)
        return PlainTextResponse('ok')