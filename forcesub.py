import asyncio
from os import environ
import os
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL')

async def ForceSub(bot: Client, cmd: Message):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(UPDATES_CHANNEL) if UPDATES_CHANNEL.startswith("-100") else UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await bot.create_chat_invite_link(chat_id=(int(UPDATES_CHANNEL) if UPDATES_CHANNEL.startswith("-100") else UPDATES_CHANNEL))
    except Exception as err:
        print(f"**Unable to do Force Subscribe to {UPDATES_CHANNEL}**\n\n**Error: {err}**")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(UPDATES_CHANNEL) if UPDATES_CHANNEL.startswith("-100") else UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="**Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/MB_Links).**",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**__š Hey [{}](tg://user?id={})**__\n š£š¹š²š®šš² šš¼š¶š» š š šØš½š±š®šš²š ššµš®š»š»š²š¹ šš¼ ššš² ššµš¶š šš¼š \n\nššš² šš¼ š¢šš²šæš¹š¼š®š±, š¢š»š¹š ššµš®š»š»š²š¹ š¦ššÆšš°šæš¶šÆš²šæš š°š®š» ššš² ššµš² šš¼š !".format(cmd.from_user.first_name, cmd.from_user.id),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ā šš¼š¶š» š š šØš½š±š®šš²š ššµš®š»š»š²š¹ ā", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("ā Verify š", url="https://t.me/RestrictedContentForwardBot?start")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Something went Wrong. Contact my [Support Group](https://t.me/MB_Links).**",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
