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
                text="**Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/DK_BOTZ).**",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**__😕 Hey [{}](tg://user?id={})**__\n 𝗣𝗹𝗲𝗮𝘀𝗲 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗕𝗼𝘁 \n\n𝗗𝘂𝗲 𝘁𝗼 𝗢𝘃𝗲𝗿𝗹𝗼𝗮𝗱, 𝗢𝗻𝗹𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗕𝗼𝘁 !".format(cmd.from_user.first_name, cmd.from_user.id),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✓ 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 ✓", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("✅ Verify 🔄", url="https://t.me/RestrictedContentForwardBot?start")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Something went Wrong. Contact my [Support Group](https://t.me/DK_BOTZ).**",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
