#(©)Codexbotz

import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 About Me 🤖", callback_data = "help")
                 ],[
                    InlineKeyboardButton('📢 Updates', url='https://t.me/mwklinks'),
                InlineKeyboardButton('💬 Support', url='https://t.me/redbullfed')
                ],[
                InlineKeyboardButton('🎟 Movies', url='https://t.me/movieworldkdy'),
                InlineKeyboardButton('🎧 Songs', url='https://t.me/mwksongs')
                ],[
                InlineKeyboardButton('👤 Developer', url='https://t.me/shamilnelli'),
                InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
  
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    text = "<b>Join My Updates Channel to use me & Enjoy the Free Service\n\n© Powered by [ __@redbullfed__ ]</b>"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>and <a href='https://t.me/{client.username}?start={argument}'>try again</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Join Updates Channel", url = client.invitelink)]])
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me") | filters.regex("ib") | filters.regex("pm") | filters.regex("dm") | filters.regex("fuck") | filters.regex("veno") | filters.regex("kitti") | filters.regex("sex") | filters.regex("vendevar"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return
WELCOME_TEXT = "<bold>Hɪ {mention} 👋</bold>\n👤 Uꜱᴇʀ Iᴅ : {id}\n\n❤️ <bold>Wᴇʟᴄᴏᴍᴇ ᴛᴏ {group_name} ❤️\n\n• Rᴜʟᴇꜱ :</bold>\n• wᴇ ᴀʀᴇ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴩ yᴏᴜ\n•ɴᴏ ᴩʀᴏᴍᴏ, ɴᴏ ᴩᴏʀɴ, ɴᴏ ᴀʙᴜꜱᴇꜱ\n• ꜱᴩᴀᴍᴍᴇʀꜱ ꜱᴛᴀy ᴀᴡᴀy\n• ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀꜱᴋ yᴏᴜʀ ꜰᴀᴠᴏʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ\n• ᴊᴜꜱᴛ ᴀꜱᴋ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ᴏɴʟy ᴅᴏɴᴛ ꜱᴇɴᴛ ʟᴀɴɢᴜᴀɢᴇꜱ ᴡɪᴛʜ ʀᴇqᴜᴇꜱᴛ\n• ᴅᴏɴᴛ ᴩᴍ ᴀɴy ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜɪꜱ ᴄʜᴀᴛ ᴡɪᴛʜᴏᴜᴛ ᴩᴇʀᴍɪꜱꜱɪᴏɴ\n•ꜱᴄʀᴀᴩᴩɪɴɢ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ᴛʜɪꜱ ɢʀᴏᴜᴩ ᴡɪʟʟ ᴍᴀᴋᴇ yᴏᴜ ꜱᴜꜰꜰᴇʀ ꜰᴏʀ ɢʟᴏʙᴀʟ ʙᴀɴꜱ ᴀɴᴅ ꜰᴇᴅ ʙᴀɴꜱ\n•ʙᴇ ꜱᴀꜰᴇ, ᴡᴇᴀʀ ᴍᴀꜱᴋ ꜱᴛᴀy ꜱᴀꜰᴇ ❤️\n\n#Sᴛᴀy Cᴏɴɴᴇᴄᴛᴇᴅ Aɴᴅ Kᴇᴇᴩ Sᴜᴩᴩᴏʀᴛ Uꜱ"
@Bot.on_message(filters.new_chat_members)
async def auto_welcome(bot: Bot, msg: Message):
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    welcome_text = f"Hey {mention}\nWelcome To {group_name}"
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          )
       )
    else:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("New Movies", url="https://t.me/joinchat/gQ8Ysfmj8zJmY2M9"),
                    InlineKeyboardButton("DVD Updates", url="t.me/mwkdvdupdates")],
                   [InlineKeyboardButton("Tech Updates", url="t.me/mwkbots"),
                    InlineKeyboardButton("Tech Support", url="t.me/redbullfed")],
                   [InlineKeyboardButton("Music World", url="t.me/mwkmusics"),
                    InlineKeyboardButton("Chat Group", url="t.me/shamilnelIi")]]))  
