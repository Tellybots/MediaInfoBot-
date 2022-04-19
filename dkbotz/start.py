# © @DKBOTZHELP Or https://github.com/DKBOTZHELP


import os
import urllib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs import Config
from dkbotz.command import command

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**👋 Hey {message.from_user.mention} ♡**

**I Am Most Powerful Media Info Bot.**

**Use Me To Generate Infomation Of Media Like Photo, Videos And Document.**

**I Also Work in Group**

**Read This For More infomation 👉 **""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('➕ Add Me To Your Group ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('📢 Bot Channel', url='http://t.me/DKBOTZ'),
            InlineKeyboardButton('💼 Support Group', url=f'http://t.me/{Config.SUPPORT_GROUP}')
            ],[
            InlineKeyboardButton('🌐 Source Code 🌐', url='https://github.com/Tellybots/Media-Info-Bot')
            ],[
            InlineKeyboardButton('⌦ Close Me ⌫', callback_data='close_data')
        ]]
        ),
     disable_web_page_preview=True
    )
