
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram import Client
from script import script  # pylint:disable=import-error
from help.access_db import db
from help.add_user import AddUserToDatabase
from plugins.forcesub import ForceSub
from config import Config
import time
import string
import shutil
import psutil
import random
import math
from help.broadcast import broadcast_handler
from pyrogram.errors import FloodWait, UserNotParticipant, MessageNotModified

#Restricted Content :-   

#Config :-   UPDATE_CHANNEL = os.environ.get("TO_CHANNEL")        BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", "True")

STAT_BUTTONS = InlineKeyboardMarkup(
    [[
     InlineKeyboardButton("♻️ Refresh ♻️", callback_data="ref_data")
    ],[
      InlineKeyboardButton("🏠", callback_data="start_data"),
      InlineKeyboardButton("❌", callback_data="close_data")
    ]]
) 

START_BUTTONS = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🤖 Bot Log", url="https://t.me/MB_Links")
            ],[
                InlineKeyboardButton("⚙️ More Help", callback_data="help_data"),
                InlineKeyboardButton("📝 About", callback_data="about_data")
            ],[
                InlineKeyboardButton("🌐 Source Code", callback_data="source_data"),
                InlineKeyboardButton("🔐 Close", callback_data="close_data")
            ]]
        )

HELP_BUTTONS = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("👥 Support", url="https://t.me/MB_Links")
            ],[
                InlineKeyboardButton("🌐 Source Code", callback_data="help_data"),
                InlineKeyboardButton("📝 About", callback_data="about_data")
            ],[
                InlineKeyboardButton("🏡 Home", callback_data="source_data"),
                InlineKeyboardButton("🔐 Close", callback_data="close_data")
            ]]
        )

ABOUT_BUTTONS = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚙️ Help", callback_data="help_data"),
                InlineKeyboardButton("❌ Close", callback_data="close"),
                InlineKeyboardButton("🏡 Home", callback_data="start_data")
            ]]
        )

SOURCE_BUTTONS = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("👨🏻‍💻 Owner", url="https://t.me/Sri_Guru05"),
                InlineKeyboardButton("🏡 Home", callback_data="start_data"),
                InlineKeyboardButton("❌ Close", callback_data="close")
            ]]
        )


MORE_BUTTONS = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚙️ Back", callback_data="help_data"),
                InlineKeyboardButton("👥 Support", url="https://t.me/MB_Links")
            ],[
                InlineKeyboardButton("🌐 Source Code", callback_data="help_data"),
                InlineKeyboardButton("📝 About", callback_data="about_data")
            ],[
                InlineKeyboardButton("🏡 Home", callback_data="source_data"),
                InlineKeyboardButton("🔐 Close", callback_data="close_data")
            ]]
        )
            
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "removebg":
        await query.message.edit_text(
            "**🙄 Select required mode**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="WITH BG", callback_data="rmbgwhite"
                        ),
                        InlineKeyboardButton(
                            text="WITHOUT BG", callback_data="rmbgplain"
                        ),
                    ],
                    [InlineKeyboardButton(text="CREATE STICKER", callback_data="rmbgsticker")
                    ],[
                     InlineKeyboardButton(text="🔙 Go Back", callback_data="photoback"),
                     InlineKeyboardButton(text="🗑 Delete", callback_data="close_data")]
                ]
            ),
        )
    elif query.data == "start_data":
        await query.message.edit_text(
            script.START_MSG.format(query.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif query.data == "help_data":
        await query.message.edit_text(
            script.HELP_MSG.format(query.from_user.mention), 
            reply_markup=HELP_BUTTONS, 
            disable_web_page_preview=True,
        )
    elif query.data == "more_data":
        await query.message.edit_text(
            script.MORE_MSG, reply_markup=MORE_BUTTONS, disable_web_page_preview=True
        )
    elif query.data == "source_data":
        await query.message.edit_text(
            script.SOURCE_MSG, reply_markup=SOURCE_BUTTONS, disable_web_page_preview=True
        )
    elif query.data == "about_data":
        await query.message.edit_text(
            script.ABOUT_MSG, reply_markup=ABOUT_BUTTONS, disable_web_page_preview=True
        )
    elif query.data == "close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()
    
    elif query.data == "stats_data":
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        total_users = await db.total_users_count()
        me = await client.get_users(query.from_user.id)
        text=f"""
**<u>🤖 BOT STATISTICS 📊</u>

● Total Disk Space: {total}
● Used Space: {used}({disk_usage}%)
● Free Space: {free} 
● CPU Usage: {cpu_usage}% 
● RAM Usage: {ram_usage}%

● Total Users in DB: {total_users}**
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"""
        text +=f"\n<b><u>👤 YOUR DETAILS</u></b>\n\n"
        text +=f"<b>● First Name: {me.first_name}</b>\n"
        text +=f"<b>● Last Name: {me.last_name}</b>\n" if me.last_name else ""
        text +=f"<b>● Username: @{me.username}</b>\n" if me.username else ""
        text +=f"<b>● User ID: {me.id}</b>\n"
        text +=f"<b>● DC ID: {me.dc_id}</b>\n" if me.dc_id else ""
        await query.message.edit(text,
                                 disable_web_page_preview=True,
                                 reply_markup=STAT_BUTTONS
                                ) 
            
    elif query.data == "ref_data":
        ref = await query.message.edit_text("__**👀 Refreshing the Data...**__")
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        total_users = await db.total_users_count()
        me = await client.get_users(query.from_user.id)
        text=f"""
**<u>🤖 BOT STATISTICS 📊</u>

● Total Disk Space: {total}
● Used Space: {used}({disk_usage}%)
● Free Space: {free} 
● CPU Usage: {cpu_usage}% 
● RAM Usage: {ram_usage}%

● Total Users in DB: {total_users}**
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"""
        text +=f"\n<b><u>👤 YOUR DETAILS</u></b>\n\n"
        text +=f"<b>● First Name: {me.first_name}</b>\n"
        text +=f"<b>● Last Name: {me.last_name}</b>\n" if me.last_name else ""
        text +=f"<b>● Username: @{me.username}</b>\n" if me.username else ""
        text +=f"<b>● User ID: {me.id}</b>\n"
        text +=f"<b>● DC ID: {me.dc_id}</b>\n" if me.dc_id else ""
        await ref.edit(text,
                       disable_web_page_preview=True,
                       reply_markup=STAT_BUTTONS
                      ) 
