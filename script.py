class script(object):

    START_MSG = """𝗛𝗲𝗹𝗹𝗼 {} ,\n𝗛𝗲𝘆,  😎\n\n𝗜 𝗔𝗺 𝗠𝗱𝗶𝘀𝗸 𝗕𝘂𝗹𝗸 𝗟𝗶𝗻𝗸 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁. 𝗜 𝗖𝗮𝗻 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗢𝘁𝗵𝗲𝗿 𝗠𝗱𝗶𝘀𝗸 𝗟𝗶𝗻𝗸. \n\n🔰 𝗜 𝗖𝗮𝗻 𝗥𝗲𝗺𝗼𝘃𝗲 𝗣𝗼𝘀𝘁 𝗶𝗻 𝗔𝗻𝗼𝘁𝗵𝗲𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗟𝗶𝗻𝗸𝘀.\n\n🔰 𝗜 𝗖𝗮𝗻 𝗕𝗼𝗹𝗱 𝗔𝗹𝗹 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀\n\n𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩 𝐒𝐞𝐧𝐝 /help\n\n👨🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :  <a href=https://t.me/Sri_Guru05>𝐁𝐨𝐭 𝐂𝐫𝐞𝐚𝐭𝐨𝐫</a>"""
    
    HELP_MSG ="""𝗛𝗲𝗹𝗹𝗼 {} ,\n𝗛𝗲𝘆,  😎\n\n𝗜 𝗔𝗺 𝗠𝗱𝗶𝘀𝗸 𝗕𝘂𝗹𝗸 𝗟𝗶𝗻𝗸 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁. 𝗜 𝗖𝗮𝗻 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗢𝘁𝗵𝗲𝗿 𝗠𝗱𝗶𝘀𝗸 𝗟𝗶𝗻𝗸. \n\n🔰 𝗜 𝗖𝗮𝗻 𝗥𝗲𝗺𝗼𝘃𝗲 𝗣𝗼𝘀𝘁 𝗶𝗻 𝗔𝗻𝗼𝘁𝗵𝗲𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗟𝗶𝗻𝗸𝘀.\n\n🔰 𝗜 𝗖𝗮𝗻 𝗕𝗼𝗹𝗱 𝗔𝗹𝗹 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀\n\n𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩 𝐒𝐞𝐧𝐝 /help\n\n👨🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :  <a href=https://t.me/Sri_Guru05>𝐁𝐨𝐭 𝐂𝐫𝐞𝐚𝐭𝐨𝐫</a>"""

    ABOUT_MSG = """🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href=https://t.me/Sri_Guru05>𝗠𝗱𝗶𝘀𝗸 𝗟𝗶𝗻𝗸 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁</a>

📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :  <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

📚 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝐇𝐨𝐬𝐭𝐞𝐝 𝐨𝐧 : <a href=https://t.me/Mdisk_Cinemas>𝐕𝐏𝐒</a>

🧑🏻‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href=https://t.me/Sri_Guru05>𝐁𝐨𝐭 𝐂𝐫𝐞𝐚𝐭𝐨𝐫</a>

👥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : <a href=https://t.me/MB_Links>𝐃𝐊 𝐁𝐎𝐓𝐙 𝐒𝐔𝐏𝐏𝐎𝐑𝐓</a>

📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href=https://t.me/MB_Links>𝐃𝐊 𝐁𝐎𝐓𝐙</a>

© 𝗕𝘆 @MB_Links 𝗧𝗲𝗮𝗺 ⭕"""

    
    MORE_MSG = """🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href=https://t.me/Sri_Guru05>𝗠𝗱𝗶𝘀𝗸 𝗟𝗶𝗻𝗸 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁</a>

📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :  <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

📚 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝐇𝐨𝐬𝐭𝐞𝐝 𝐨𝐧 : <a href=https://t.me/Mdisk_Cinemas>𝐕𝐏𝐒</a>

🧑🏻‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href=https://t.me/Sri_Guru05>𝐁𝐨𝐭 𝐂𝐫𝐞𝐚𝐭𝐨𝐫</a>

👥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : <a href=https://t.me/MB_Links>𝐃𝐊 𝐁𝐎𝐓𝐙 𝐒𝐔𝐏𝐏𝐎𝐑𝐓</a>

📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href=https://t.me/MB_Links>𝐃𝐊 𝐁𝐎𝐓𝐙</a>

© 𝗕𝘆 @MB_Links 𝗧𝗲𝗮𝗺 ⭕"""

    
    SOURCE_MSG = """https://t.me/MB_Links/118"""
 
