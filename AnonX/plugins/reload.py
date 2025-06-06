import asyncio

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

from config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.misc import db
from AnonX.utils.database import get_authuser_names, get_cmode
from AnonX.utils.decorators import (ActualAdminCB, AdminActual,
                                         language)
from AnonX.utils.formatters import alpha_to_int
from strings.filters import command

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")
import requests

async def check_subscription(user_id):
    channel_username = "KU_KX"  # معرف القناة الفعلي

    bot_token = "6046893597:AAE3zOhlKW3gferXfWXgc0aH6LSy5HJk4z4"  # رمز معرف البوت الخاص بك
    api_url = f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@{channel_username}&user_id={user_id}"
    
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200 and data["ok"]:
        status = data["result"]["status"]
        if status == "left":
            return False
        else:
            return True

    return False

@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_message(
    command(["ريلود"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    user_id = message.from_user.id

    # التحقق من اشتراك المستخدم في القناة
    is_subscribed = await check_subscription(user_id)
    if not is_subscribed:
        channel_name = "على شُرفَةِ الانْتِظار"
        channel_url = "https://t.me/KU_KX"
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(channel_name, url=channel_url)]]
        )
        return await message.reply_text(
            "⚠️︙عذراً، عليك الانضمام الى قناة البوت أولاً :",
            reply_markup=keyboard
        )
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "⌯︙فشل في تحميل الادمنيه."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_message(
    command(["اعادة تشغيل بوت هولي"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"⌯︙جار اعادة تشغيل {MUSIC_BOT_NAME} في هذه الدردشه."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Anon.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Anon.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"⌯︙تم اعادة تشغيل {MUSIC_BOT_NAME} لهذه الدردشه, هسه تكدر ترجع تشغل..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "⌯︙التحميل مكتمل بالفعل.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "⌯︙تم انتهاء التحميل او تم الغائهُ.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "⌯︙تم الغاء التحميل.", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"⌯︙تم الغاء بدء التحميل بواسطة {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "⌯︙فشل في الغاء التحميل...", show_alert=True
            )
    await CallbackQuery.answer(
        "⌯︙فشل في معالجة الطلب.", show_alert=True
    )
