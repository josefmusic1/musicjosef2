import requests
import json
from AnonX import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters


url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(text) -> str:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except Exception as e:
        return "عذراً، حدث خطأ أثناء التواصل مع الذكاء الاصطناعي."

def reply_gpt(client, message):
    try:
        text = message.text.split("/gpt ", 1)[1]
    except IndexError:
        client.send_message(
            chat_id=message.chat.id,
            text="يرجى كتابة سؤالك بعد الأمر /gpt.",
            reply_to_message_id=message.message_id
        )
        return

    reply_text = gpt(text)
    chat_id = message.chat.id
    if message.reply_to_message is not None:
        message_id = message.reply_to_message.message_id
    else:
        message_id = None
    client.send_message(
        chat_id=chat_id,
        text=reply_text + "\n\n\nتم استخدام الذكاء الاصطناعي للإجابة على سؤالك.",
        reply_to_message_id=message_id
    )

@app.on_message(filters.command("gpt"))
def reply(client, message):
    message.reply_text("تم استلام سؤالك، يرجى الانتظار حتى يتم الرد عليك بواسطة الذكاء الاصطناعي...")
    reply_gpt(client, message)
