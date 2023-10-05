from aiogram import F
from aiogram import Router
from aiogram.types import Message

from bot.config_data import config_dict

router = Router(name="print_router")


@router.message(F.text.lower().contains("печат"))
async def print_filter(message: Message):

    await message.bot.send_message(chat_id=config_dict["admin_id"], text="check group")
    # await message.bot.send_message(chat_id=config_dict["manager_id"], text="check group")