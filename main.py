import requests
import telebot
from telebot import types

# DEV: kudodz
# Telegram: @kudo1004

token = "TOKEN CỦA BẠN"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["tt"])
def get_info_tk(message):
    allowed_group_id = -4696880436 # id nhóm đc cho phép

    if message.chat.id != allowed_group_id:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Liên Hệ Admin", url="https://t.me/kudo1004"))
        bot.reply_to(message, "❌ Lệnh Này Chỉ Sử Dụng Được Trong Nhóm Chính Thức! Nhóm Chính Thức: https://t.me/+ZqnS4nIlsCo0MWRl", reply_markup=markup)
        return

    command_parts = message.text.split()
    if len(command_parts) < 2:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Liên Hệ Admin", url="https://t.me/kudo1004"))
        bot.reply_to(message, "❌ Câu Lệnh Không Hợp Lệ. Hãy Sử Dụng: /tt username", reply_markup=markup)
        return

    username = command_parts[1]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Liên Hệ Admin", url="https://t.me/kudo1004"))

    try:
        url = f"http://145.223.80.56:5009/info_tiktok?username={username}"
        res = requests.get(url, timeout=10)
        data = res.json()

        msg = f"""
<b>📊 Thông Tin Tài Khoản TikTok @{data.get('username', 'N/A')}</b>

<b>✨ Thống Kê Tài Khoản</b>
<code>👥 Người theo dõi:</code> <b>{data.get('followers', 'N/A')}</b>
<code>👤 Số người đang theo dõi:</code> <b>{data.get('following', 'N/A')}</b>
<code>❤️ Tổng Số Tim:</code> <b>{data.get('hearts', 'N/A')}</b>
<code>🎬 Tổng Số Video Đã Đăng:</code> <b>{data.get('videos', 'N/A')}</b>

<b>🔒 Chi Tiết Tài Khoản:</b>
<code>📛 Tên Hiển Thị:</code> <b>{data.get('name', 'N/A')}</b>
<code>👤 Tên Người Dùng:</code> <b>@{data.get('username', 'N/A')}</b>
<code>🆔 Số ID Người Dùng:</code> <b>{data.get('user_id', 'N/A')}</b>
<code>🔒 Tài Khoản Riêng Tư:</code> <b>{'Có 🔐' if data.get('is_private') else 'Không 🔓'}</b>
<code>⭐ Mở Phần Yêu Thích:</code> <b>{'Có ✅' if data.get('open_favorite') else 'Không ❌'}</b>

<b>📝 Tiểu Sử:</b>
<code>{data.get('signature', 'Người Này Không Có Bio.')}</code>

<b>🔐 Thông Tin Kỹ Thuật:</b>
<code>🔒 Sec UID:</code> <code>{data.get('sec_uid', 'N/A')}</code>
<code>🖼️ Ảnh Đại Diện:</code> <a href="{data.get('profile_picture', '#')}">Xem Hình Ảnh</a>
"""
        bot.reply_to(message, msg, reply_markup=markup, parse_mode="HTML")

    except Exception as e:
        print(f"😭 Lỗi Kết Nối API: {e} | Developer: @kudo1004")
        bot.reply_to(message, "⚠️ Lỗi Kết Nối API", reply_markup=markup)



print("🤖 Bot Đang Chạy!")
print("telegram: @kudo1004")
bot.infinity_polling()
