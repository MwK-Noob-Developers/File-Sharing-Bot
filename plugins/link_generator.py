#(©)Codexbotz
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, User
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id
import asyncio

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=30)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=30)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=30)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

@Bot.on_message(filters.new_chat_members)
async def welcomey(bot, message):
        chat_id=message.chat.id,
	AutoDelete = await bot.reply_text(
            text=f"<b>Hɪ {message.from_user.mention} 👋</b>\n👤 Uꜱᴇʀ Iᴅ : {message.from_user.id}\n\n❤️ <b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ {message.chat.title} ❤️\n\n• Rᴜʟᴇꜱ :</b>\n• wᴇ ᴀʀᴇ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴩ yᴏᴜ\n•ɴᴏ ᴩʀᴏᴍᴏ, ɴᴏ ᴩᴏʀɴ, ɴᴏ ᴀʙᴜꜱᴇꜱ\n• ꜱᴩᴀᴍᴍᴇʀꜱ ꜱᴛᴀy ᴀᴡᴀy\n• ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀꜱᴋ yᴏᴜʀ ꜰᴀᴠᴏʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ\n• ᴊᴜꜱᴛ ᴀꜱᴋ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ᴏɴʟy ᴅᴏɴᴛ ꜱᴇɴᴛ ʟᴀɴɢᴜᴀɢᴇꜱ ᴡɪᴛʜ ʀᴇqᴜᴇꜱᴛ\n• ᴅᴏɴᴛ ᴩᴍ ᴀɴy ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜɪꜱ ᴄʜᴀᴛ ᴡɪᴛʜᴏᴜᴛ ᴩᴇʀᴍɪꜱꜱɪᴏɴ\n•ꜱᴄʀᴀᴩᴩɪɴɢ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ᴛʜɪꜱ ɢʀᴏᴜᴩ ᴡɪʟʟ ᴍᴀᴋᴇ yᴏᴜ ꜱᴜꜰꜰᴇʀ ꜰᴏʀ ɢʟᴏʙᴀʟ ʙᴀɴꜱ ᴀɴᴅ ꜰᴇᴅ ʙᴀɴꜱ\n•ʙᴇ ꜱᴀꜰᴇ, ᴡᴇᴀʀ ᴍᴀꜱᴋ ꜱᴛᴀy ꜱᴀꜰᴇ ❤️\n\n<b>#Sᴛᴀy Cᴏɴɴᴇᴄᴛᴇᴅ Aɴᴅ Kᴇᴇᴩ Sᴜᴩᴩᴏʀᴛ Uꜱ</b>", 
            reply_markup=InlineKeyboardMarkup([
                                               [InlineKeyboardButton("New Movies", url="https://t.me/joinchat/gQ8Ysfmj8zJmY2M9"),
                                                InlineKeyboardButton("DVD Updates", url="t.me/mwkdvdupdates")],
                                               [InlineKeyboardButton("Tech Updates", url="t.me/mwkbots"),
                                                InlineKeyboardButton("Tech Support", url="t.me/redbullfed")],
                                               [InlineKeyboardButton("Music World", url="t.me/mwkmusics"),
                                                InlineKeyboardButton("Chat Group", url="t.me/shamilnelIi")],
                                              ])
            )
            await asyncio.sleep(35)
            await AutoDelete.delete()
