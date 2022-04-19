from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

# Delete Messages
@Client.on_callback_query(filters.regex("close_data"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
