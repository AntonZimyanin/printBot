from aiogram import F
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart   

from bot.keyboards.user_kb import get_user_kb


router = Router(name="user_router")


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        """
Welcome to the printBot.
Частые вопросы:                             
""",
        reply_markup=get_user_kb()
    )


@router.callback_query(F.data == "В каком блоке печатают?")
async def send_location(callback: CallbackQuery):
    await callback.message.answer(
        "Печатают в Б93"
    )


@router.callback_query(F.data == "Цена печати одного листа")
async def send_price(callback: CallbackQuery):
    await callback.message.answer(
        "Цена печати одного листа — 20коп."
    )