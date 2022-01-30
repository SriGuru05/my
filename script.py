class script(object):

    START_MSG = """𝗛𝗲𝗹𝗹𝗼 {} ,\n𝗜 𝗔𝗺 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗠𝗼𝘀𝘁 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗲𝗱 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝗕𝗼𝘁\n\n𝗨𝘀𝗲 𝗠𝗲 𝗧𝗼 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝗔𝗹𝗹 𝗧𝘆𝗽𝗲𝘀 𝗢𝗳 𝗠𝗲𝗱𝗶𝗮 𝗟𝗶𝗸𝗲 𝗣𝗵𝗼𝘁𝗼, 𝗙𝗶𝗹𝗲𝘀, 𝗩𝗶𝗱𝗲𝗼, 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗘𝘁𝗰\n\n● 𝗜 𝗔𝗹𝘀𝗼 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗔𝗻𝗱 𝗣𝘂𝗯𝗹𝗶𝗰 𝗖𝗵𝗮𝗻𝗻𝗲𝗹.\n\n● 𝗜 𝗔𝗹𝘀𝗼 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝗙𝗿𝗼𝗺 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹.\n\n𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗜𝗻𝗳𝗼 𝗦𝗲𝗻𝗱 /help\n\n👨🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :  <a href=https://t.me/DKBOTZHELP>𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬</a>"""
    
    HELP_MSG = """𝗛𝗲𝗹𝗹𝗼 {} \n\n𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀:-\n\n/copy - 𝗧𝗼 𝗰𝗼𝗽𝘆 𝗮 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗠𝗲𝘀𝘀𝗮𝗴𝗲\n/forward - 𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗳𝗼𝗿𝘄𝗮𝗿𝗱𝗶𝗻𝗴 𝗠𝗲𝘀𝘀𝗮𝗴𝗲\n/total - 𝗖𝗼𝘂𝗻𝘁 𝘁𝗼𝘁𝗮𝗹 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝗗𝗕\n/status - 𝗖𝗵𝗲𝗰𝗸 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝘁𝗮𝘁𝘂𝘀\n/help - 𝗛𝗲𝗹𝗽 𝗱𝗮𝘁𝗮\n/about - 𝗕𝗼𝘁 𝗜𝗻𝗳𝗼\n/stop - 𝗧𝗼 𝘀𝘁𝗼𝗽 𝗮𝗹𝗹 𝗿𝘂𝗻𝗻𝗶𝗻𝗴 𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗲𝘀.\n\n𝗨𝘀𝗲 /copy 𝗧𝗼 𝗖𝗼𝗽𝘆 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗙𝗿𝗼𝗺 𝗔 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲.\n𝗔𝗳𝘁𝗲𝗿 𝗖𝗼𝗽𝘆 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗦𝘁𝗮𝗿𝘁 𝗙𝗼𝗿𝘄𝗮𝗿𝗱𝗶𝗻𝗴 𝗕𝘆 𝗨𝘀𝗶𝗻𝗴 /forward.\n\n𝗬𝗼𝘂 𝗪𝗶𝗹𝗹 𝗚𝗲𝘁 𝗬𝗼𝘂𝗿 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝗙𝗶𝗹𝗲 𝗶𝗻 𝗧𝗵𝗶𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :-  @RestrictedContentForwardLog\n\n© 𝗕𝘆 @DKBOTZFUTURE 𝐓𝐞𝐚𝐦 ❤️"""
    
    ABOUT_MSG = """🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href=https://t.me/RestrictedContentForwardBot>𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐁𝐨𝐭 </a>

📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :  <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

📚 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝐇𝐨𝐬𝐭𝐞𝐝 𝐨𝐧 : <a href=https://t.me/DKBOTZFUTURE>𝐕𝐏𝐒</a>

🧑🏻‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href=https://t.me/DKBOTZHELP>𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬</a>

👥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : <a href=https://t.me/DK_BOTZ>𝐃𝐊 𝐁𝐎𝐓𝐙 𝐒𝐔𝐏𝐏𝐎𝐑𝐓</a>

📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href=https://t.me/DKBOTZ>𝐃𝐊 𝐁𝐎𝐓𝐙</a>

© 𝗕𝘆 @DKBOTZFUTURE 𝗧𝗲𝗮𝗺 ⭕"""

    
    MORE_MSG = """🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href=https://t.me/RestrictedContentForwardBot>𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐁𝐨𝐭 </a>

📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :  <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

📚 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝐇𝐨𝐬𝐭𝐞𝐝 𝐨𝐧 : <a href=https://t.me/DKBOTZFUTURE>𝐕𝐏𝐒</a>

🧑🏻‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href=https://t.me/DKBOTZHELP>𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬</a>

👥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : <a href=https://t.me/DK_BOTZ>𝐃𝐊 𝐁𝐎𝐓𝐙 𝐒𝐔𝐏𝐏𝐎𝐑𝐓</a>

📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href=https://t.me/DKBOTZ>𝐃𝐊 𝐁𝐎𝐓𝐙</a>

© 𝗕𝘆 @DKBOTZFUTURE 𝗧𝗲𝗮𝗺 ⭕"""

    
    SOURCE_MSG = """⭕️ आवश्यक सूचना ⭕️

🔰 अगर आपको 𝗠𝗱𝗶𝘀𝗸 𝗕𝗼𝘁 का 𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲 चाहिए तो आप ₹3000 𝗣𝗮𝘆 करके हमें 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁 भेजें और आप रुपया नहीं देना चाहते हैं तो टेलीग्राम  10𝗸 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 चैनल वाला  आपको देना होगा तभी मिलेगा। चैनल देने के लिए @Mdisk_By_Bot पर संपर्क करें ।

𝗕𝗮𝗻𝗸 𝗗𝗲𝘁𝗮𝗶𝗹𝘀 𝗙𝗼𝗿 𝗠𝗼𝗻𝗲𝘆 𝗧𝗿𝗮𝗻𝘀𝗳𝗲𝗿

Account Holder Name : `MR MONU KUMAR PURI`
Account Number : `30098100093971`
Bank Name : `Bank of Baroda`
IFSC CODE : `BARB0SIWANX`


𝗦𝗲𝗻𝗱 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁 𝗧𝗼 :- @Mdisk_By_Bot

𝗜𝗳 𝗔𝗻𝘆 𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝗧𝗼 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- @Mdisk_By_Bot"""
 
