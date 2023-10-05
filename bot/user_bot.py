from aiogram import F
from aiogram import Router
from aiogram.types import Message, CallbackQuery

from bot.keyboards.user_kb import get_user_kb


router = Router(name="user_router")



#"Общая информация"
@router.callback_query(F.data == "Общая информация")
async def general_data(callback: CallbackQuery):
    await callback.message.edit_text(
        "Общая информация", reply_markup=get_user_kb()
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


@router.callback_query(F.data == "Можно ли прийти с флешкой?")
async def can_bring_flash(callback: CallbackQuery):
    await callback.message.answer(
        "Да, можно, главное — не Dead Drops)"
    )