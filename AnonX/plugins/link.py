import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from strings.filters import command
from pyrogram.types import Message
from AnonX import app
from strings.filters import command
from strings.filters import command

@app.on_message(
    command(["هولي"])
    & ~filters.edited
)
async def ahmed(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/pvK757Rc/image.jpg",
        caption=f"""◉ على شُرفَةِ الانْتِظار : ❪[𓏺 على شُرفَةِ الانْتِظار. ⟭ཊ ˼](https://t.me/KU_KX)❫
◉ Dev : ❪ @KU_LX ❫
◉ 𝙸𝙳 : ❪ 399401433 ❫
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "جـوزيـّـف ϟ ¹", url=f"https://t.me/KU_LX"),
                ],[
                    InlineKeyboardButton(
                        "على شُرفَةِ الانْتِظار.", url=f"https://t.me/KU_KX"),
                ],
            ]
        ),
    )
