"""
Module that implements VK Callback API
"""
from fastapi import FastAPI, Response, Request
from config import TOKEN_CONF_VK
from telegram import BotMessage

app = FastAPI()


@app.post("/")
async def vk_handler(req: Request):
    """
    To handle VK request, parsing and execute bot or confirmation
    :param req: vk request
    :return: response ok or confirmation code
    """
    try:
        data = await req.json()
    except Exception:
        print("Empty request")
        return Response("not today", status_code=403)

    if data["type"] == "confirmation":
        print("Send confirmation token: {}", TOKEN_CONF_VK)
        return Response(TOKEN_CONF_VK)

    if data["type"] == "wall_post_new":
        message = BotMessage()
        for attachment in data["object"]["attachments"]:
            if attachment['type'] == "photo":
                for size in attachment["photo"]["sizes"]:
                    if size['type'] == 'x':
                        message.add_media(size['url'], caption=data['object']['text'])
        message.push()
        return Response("ok")
    return Response("ok")

