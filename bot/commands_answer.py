from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import CommandStart   

from bot.keyboards.user_kb import get_user_kb, get_start_kb
from bot.keyboards.print_type_kb import get_print_type_kb


router = Router(name="user-commands")


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        """
Привет \U0001F64B,
Что вас интересует?
""",
        reply_markup=get_start_kb()
    )


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


@router.message(Command("payment_methods"))
async def payment_methods(message: Message):
    await message.answer("""
Способы оплаты:       
- налик
- беларусбанк
- белинвест
- QR-код в оплати                                                                                            
""")