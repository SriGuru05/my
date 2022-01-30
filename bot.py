from os import environ
import os
import time
from unshortenit import UnshortenIt
from urllib.request import urlopen
from urllib.parse import urlparse
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyshorteners import Shortener
from forcesub import ForceSub
from bs4 import BeautifulSoup
#from doodstream import DoodStream
import requests
import re

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
DATABASE_URI = environ.get('DATABASE_URI')
BOT_USERNAME = environ.get('BOT_USERNAME')
CHANNEL = environ.get('CUSTOM_FOOTER')
MDISK_TOKEN = environ.get('MDISK_TOKEN')
bot = Client('Doodstream bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=0)


START_MSG="𝗛𝗲𝗹𝗹𝗼 {} ,\n𝗛𝗲𝘆,  😎\n\n𝗜 𝗔𝗺 𝗠𝗱𝗶𝘀𝗸 𝗕𝘂𝗹𝗸 𝗟𝗶𝗻𝗸 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁. 𝗜 𝗖𝗮𝗻 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗢𝘁𝗵𝗲𝗿 𝗠𝗱𝗶𝘀𝗸 𝗟𝗶𝗻𝗸. \n\n🔰 𝗜 𝗖𝗮𝗻 𝗥𝗲𝗺𝗼𝘃𝗲 𝗣𝗼𝘀𝘁 𝗶𝗻 𝗔𝗻𝗼𝘁𝗵𝗲𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗟𝗶𝗻𝗸𝘀.\n\n🔰 𝗜 𝗖𝗮𝗻 𝗕𝗼𝗹𝗱 𝗔𝗹𝗹 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀\n\n𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩 𝐒𝐞𝐧𝐝 /help\n\n👨🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :  <a href=https://t.me/DKBOTZHELP>Bot Creater</a>"

buttons=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🤖 Bot Forward Channel", url="https://t.me/RestrictedContentForwardLog")
            ],[
                InlineKeyboardButton("⚙️ Help", callback_data="help_data"),
                InlineKeyboardButton("📝 About", callback_data="about_data")
            ],[
                InlineKeyboardButton("🌐 Source Code", callback_data="source_data"),
                InlineKeyboardButton("🔐 Close", callback_data="close_data")
            ]]
        )




@bot.on_message(filters.private & filters.command('start'))
async def start(bot, message):
    Fsub = await ForceSub(bot, message)
    if Fsub == 400:
        return
    await bot.send_message(
        chat_id=message.chat.id,
        text=START_MSG.format(
                message.from_user.first_name),
        reply_markup=buttons,
        disable_web_page_preview=True,
        parse_mode="html")

   
@bot.on_message(filters.text & filters.private)
async def Doodstream_uploader(bot, message):
    new_string = str(message.text)
    conv = await message.reply("Wait..... Few Seconds ✋")
    dele = conv["message_id"]
    try:
        Doodstream_link = await multi_Doodstream_up(new_string)
        await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
        await message.reply(f'**{Doodstream_link}**' , quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


@bot.on_message(filters.photo & filters.private)
async def Doodstream_uploader(bot, message):
    new_string = str(message.caption)
    conv = await message.reply("Wait..... Few Seconds ✋")
    dele = conv["message_id"]
    try:
        Doodstream_link = await multi_Doodstream_up(new_string)
        if(len(Doodstream_link) > 1020):
            await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
            await message.reply(f'{Doodstream_link}' , quote=True)
        else:
            await bot.delete_messages(chat_id=message.chat.id, message_ids=dele)
            await bot.send_photo(message.chat.id, message.photo.file_id, caption=f'**{Doodstream_link}**')
            await bot.send_photo(-1001605465041, message.photo.file_id, caption=f'**{Doodstream_link}**')
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


'''async def get_ptitle(url):
    if ('bit' in url ):
      url = urlopen(url).geturl()
      
      
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    for title in soup.find_all('title'):
        pass
    title = list(title.get_text())
    title = title[8:]
    str = 't.me/' + CHANNEL + ' '
    for i in title:
        str = str + i
    lst = list(html_text.split(","))
    c = 0
    for i in lst:
        if ("""/e/""" in i):
            found = lst[c]
            break
        c += 1

    # Doodstream.com link
    Doodstream_video_id = list(found.split(":"))
    video_id = Doodstream_video_id[2]
    video_id = list(video_id.split(","))
    v_id = video_id[0]
    #v_len = len(v_id)
    #v_id = v_id[1:v_len - 2]

    v_url = 'https://vidzoop.blogspot.com/p/share-video.html?vid=' + v_id + '&m=1'
    v_url = url
    res = [str, v_url]
    return res'''


async def Doodstream_up(link):
    if ('bit' in link ):
        #link = urlopen(link).geturl()
        unshortener = UnshortenIt()
        link = unshortener.unshorten(link)
    
    title_new = urlparse(link)
    title_new = os.path.basename(title_new.path)
    title_Doodstream = '@' + CHANNEL + title_new
    realaurl = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
    param = {'token':f'{MDISK_TOKEN}','link':link}
    res = requests.post(realaurl, json = param)         
    data = res.json()
    data = dict(data)
    print(data)
    #bot.delete_messages(con)
    v_url = data['sharelink']
    return (v_url)


async def multi_Doodstream_up(ml_string):
    list_string = ml_string.splitlines()
    ml_string = ' \n'.join(list_string)
    new_ml_string = list(map(str, ml_string.split(" ")))
    new_ml_string = await remove_username(new_ml_string)
    new_join_str = "".join(new_ml_string)

    urls = re.findall(r'(https?://[^\s]+)', new_join_str)

    nml_len = len(new_ml_string)
    u_len = len(urls)
    url_index = []
    count = 0
    for i in range(nml_len):
        for j in range(u_len):
            if (urls[j] in new_ml_string[i]):
                url_index.append(count)
        count += 1
    new_urls = await new_Doodstream_url(urls)
    url_index = list(dict.fromkeys(url_index))
    i = 0
    for j in url_index:
        new_ml_string[j] = new_ml_string[j].replace(urls[i], new_urls[i])
        i += 1

    new_string = " ".join(new_ml_string)
    return await addFooter(new_string)


async def new_Doodstream_url(urls):
    new_urls = []
    for i in urls:
        time.sleep(0.2)
        new_urls.append(await Doodstream_up(i))
    return new_urls


async def remove_username(new_List):
    for i in new_List:
        if('@' in i or 't.me' in i or 'https://bit.ly/abcd' in i or 'https://bit.ly/123abcd' in i or 'telegra.ph' in i or 'T.ME' in i or 'T.me' in i or 't.ME' in i):
            new_List.remove(i)
    return new_List

async def addFooter(str):
    footer = """

""" + CHANNEL + """ """
    return str + footer

bot.run()
