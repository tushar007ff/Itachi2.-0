from Rudra import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode

random_photo = [
    "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg" "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg" "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg" "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg" "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c8
]
# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

bg_path = "Rudra/assets/userinfo.png"
font_path = "Rudra/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #

# Function to handle both new members and members who have left
async def handle_member_update(client: app, member: ChatMemberUpdated):
    chat = member.chat

    count = await app.get_chat_members_count(chat.id)

    user = member.new_chat_member.user if member.new_chat_member else member.old_chat_member.user
    try:
        if user.photo:
            # User has a profile photo
            photo = await app.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user.id,
                profile_path=photo,
            )
        else:
            # User doesn't have a profile photo, use random_photo directly
            welcome_photo = random.choice(random_photo)

        # Assuming you have a way to obtain the member count


        if member.new_chat_member:
            # Welcome message for new members
            caption = (
            f"**🌷𝐇ᴇʏ {member.new_chat_member.user.mention}**\n\n**🏘𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
            f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {chat.title}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**💖𝐔ʀ 𝐈d: {member.new_chat_member.user.id}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**✍️𝐔ʀ 𝐔.𝐍: @{member.new_chat_member.user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            button_text = "๏ ᴠɪᴇᴡ ᴘʀᴏғɪʟᴇ ๏"
        else:
            # Farewell message for members who have left
            caption = f"**❅─────✧❅✦❅✧─────❅**\n\n**๏ ᴀ ᴍᴇᴍʙᴇʀ ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ🥀**\n\n**➻** {member.old_chat_member.user.mention}\n\n**๏ ɢᴏᴏᴅʙʏᴇ ᴀɴᴅ ʜᴏᴘᴇ ᴛᴏ sᴇᴇ ʏᴏᴜ ᴀɢᴀɪɴ sᴏᴏɴ ɪɴ ᴛʜɪs ᴄᴜᴛᴇ ɢʀᴏᴜᴘ✨**\n\n**ㅤ•─╼⃝𖠁 ʙʏᴇ ♡︎ ʙᴀʙʏ 𖠁⃝╾─•**"
            button_text = "๏ ᴠɪᴇᴡ ʟᴇғᴛ ᴍᴇᴍʙᴇʀ ๏"

        # Generate a deep link to open the user's profile
        deep_link = f"tg://openmessage?user_id={user.id}"

        # Send the message with the photo, caption, and button
        await client.send_photo(
            chat_id=member.chat.id,
            photo=welcome_photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(button_text, url=deep_link)]
            ])
        )
    except RPCError as e:
        print(e)
        return

# Connect the function to the ChatMemberUpdated event
@app.on_chat_member_updated(filters.group, group=20)
async def member_update_handler(client: app, member: ChatMemberUpdated):
    await handle_member_update(client, member)
