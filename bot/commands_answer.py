from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.config_data import config_dict
from bot.keyboards.user_kb import get_user_kb
from bot.keyboards.print_type_kb import get_print_type_kb



router = Router(name="user-commands")


@router.message(Command("help"))
async def change_settings(message: Message):
    await message.answer("""
Привет \U0001F64B,
здесь ты можешь:
\U0001F4E6 /online_order — сдeлать онлайн заказ
\U00002753 /faq — посмотреть интересующую информацию
""")

    
@router.message(Command("faq"))
async def change_settings(message: Message):
    await message.answer(
        "Общая информация", reply_markup=get_user_kb()
    )


@router.message(Command("online_order"))
async def change_settings(message: Message):
    await message.answer(
        "Выберите тип печати", reply_markup=get_print_type_kb()
    )