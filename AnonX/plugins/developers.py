import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المطور","جوزيف","مطور السورس","مبرمج السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/pvK757Rc/image.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 جـوزيـّـف ϟ ¹ ˼](https://t.me/KU_LX)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @KU_LX ❫
◉ 𝙸𝙳   : ❪ 399401433 ❫
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "جـوزيـّـف ϟ ¹", url=f"https://t.me/KU_LX"), 
                 ],[
                   InlineKeyboardButton(
                        "⌞ على شُرفَةِ الانْتِظار ⌝", url=f"https://t.me/KU_KX"),
                ],

            ]

        ),

    )
