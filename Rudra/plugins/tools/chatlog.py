import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from Rudra import app  

photo = [
    "https://te.legra.ph/file/7757731c3e8b784b6a550.png", 
    "https://te.legra.ph/file/58c34981e21180989887c.png", 
    "https://te.legra.ph/file/a3a874be5095d9af685ac.png", 
    "https://te.legra.ph/file/ac461a1889255424420ff.png", 
    "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", 
    "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", 
    "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", 
    "https://te.legra.ph/file/ab243bcad20965f637b5c.png", 
    "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", 
    "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", 
    "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", 
    "https://te.legra.ph/file/700af8c3ee786a20aff35.png", 
    "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", 
    "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", 
    "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", 
    "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", 
    "https://te.legra.ph/file/1b55fe681163188149fa4.png", 
    "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", 
    "https://te.legra.ph/file/30b121ce5fa87360692ba.png", 
    "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", 
    "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", 
    "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", 
    "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", 
    "https://te.legra.ph/file/639efe98c133d71c418db.png", 
    "https://te.legra.ph/file/8a834586b677739b86bff.png", 
    "https://te.legra.ph/file/13f79674ce777f43871fb.png", 
    "https://te.legra.ph/file/147157eca055a1e2c8756.png", 
    "https://te.legra.ph/file/b774a8da74dc954afebc6.png", 
    "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", 
    "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", 
    "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", 
    "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", 
    "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", 
    "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", 
    "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", 
    "https://telegra.ph/file/1b80eec8135011abbe532.jpg", 
    "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", 
    "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", 
    "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", 
    "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", 
    "https://telegra.ph/file/15305e45af3139022a789.jpg", 
    "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", 
    "https://graph.org/file/597fb01053d7d19454a56.jpg", 
    "https://graph.org/file/8d9f37781edef499e6240.jpg", 
    "https://graph.org/file/8f792296f4cb01f207521.jpg", 
    "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", 
    "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg",
    "https://graph.org/file/598c181eb136ae92aa107.jpg", 
    "https://graph.org/file/59a167ff606909e30ad73.jpg", 
    "https://graph.org/file/8084b560bd19d28caae87.jpg", 
    "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**ʜᴇʏ {message.from_user.mention}**\n\n**🏘ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ʟᴏᴠᴇ ʏᴏᴜ ᴅᴏsᴛ🥳**\n\n"
            f"**ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**ᴄʜᴀᴛ ᴜ.ɴ: @{chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**ᴜʀ ɪᴅ: {member.new_chat_member.user.id}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**ᴜʀ ᴜ.ɴ: @{member.new_chat_member.user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**ᴄᴏᴍᴘʟᴇᴛᴇᴅ {count} ᴍᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"ᴡᴇʟᴄᴏᴍᴇ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ🥳\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"ᴄʜᴀᴛ ᴜ.ɴ: @{message.chat.username}\n"
                f"ᴜʀ ɪᴅ: {member.id}\n"
                f"ᴜʀ ᴜ.ɴaмe: @{member.username}\n"
                f"ᴄᴏᴍᴘʟᴇᴛᴇᴅ {count} ᴍᴇᴍʙᴇʀ𝐬🎉"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝐊ɪᴅɴᴀᴘ 𝐌ᴇ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


