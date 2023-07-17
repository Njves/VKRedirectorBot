from fastapi import FastAPI
from pydantic import BaseModel
from config import TOKEN_VK, TOKEN_CONF_VK
from datetime import datetime


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


class Attachment:
    type: str
    photo: Photo


class Post(BaseModel):
    id: str
    date: datetime
    text: str
    attachments: list[Attachment]


class Event(BaseModel):
    type: str
    event_id: str
    v: float
    group_id: str
    object: Post


app = FastAPI()


@app.post("/")
async def create_item(query: str):
    event: Event = Event.parse_raw(query)
    match event.type:
        case 'confirmation':
            return TOKEN_CONF_VK
        case 'wall_post_new':
            print(event.object)