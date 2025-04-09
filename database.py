import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)")
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

from aiogram import Router, types
from database import add_user

router = Router()

@router.message()
async def save_user(message: types.Message):
    add_user(message.from_user.id)

from aiogram import Router, Bot, types
from aiogram.filters import Command
from config import ADMIN_IDS
from database import get_all_users

router = Router()

@router.message(Command("notify"))
async def send_notifications(message: types.Message, bot: Bot):
    if message.from_user.id not in ADMIN_IDS:
        return

    text = message.text.replace("/notify", "").strip()
    if not text:
        await message.answer("⚠️ Введите сообщение после команды /notify")
        return

    users = get_all_users()
    for user_id in users:
        try:
            await bot.send_message(user_id, f"📢 Уведомление от администратора:\n\n{text}")
        except Exception:
            pass
    await message.answer("✅ Уведомления отправлены.")
