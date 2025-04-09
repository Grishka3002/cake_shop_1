from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

router = Router()

# Главное меню
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📜 Меню и условия заказа")],
        [KeyboardButton(text="📩 Связаться с администратором")]
    ],
    resize_keyboard=True
)

# Обработчик меню
@router.message(Command("start"))
async def show_menu(message: types.Message):
    await message.answer("Выберите нужный раздел:", reply_markup=menu_kb)

# Обработчик кнопки меню
@router.message(lambda message: message.text == "📜 Меню и условия заказа")
async def send_menu(message: types.Message):
    await message.answer("📝 Вот наше меню:\n\n"
                         "🍫 Шоколадный торт - 1000₽\n"
                         "🍰 Ванильный торт - 900₽\n"
                         "🍓 Фруктовый торт - 1100₽\n\n"
                         "📌 Условия заказа: предзаказ за 2 дня.")
