from aiogram import Router, types
from config import ADMIN_IDS

router = Router()

# Обработчик сообщений от пользователя
@router.message(lambda message: message.text == "📩 Связаться с администратором")
async def contact_admin(message: types.Message):
    await message.answer("Напишите ваш вопрос, и администратор ответит вам.")

# Пересылка сообщений администратору
@router.message()
async def forward_to_admin(message: types.Message):
    for admin_id in ADMIN_IDS:
        await message.forward(admin_id)
    await message.answer("✅ Ваше сообщение отправлено администратору.")
