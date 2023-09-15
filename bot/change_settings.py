from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config_data import config_data


router = Router(name="change_settings")


@router.message(Command("change_settings"))
async def change_settings(message: Message):

    config_dict = config_data("config.json")

    if message.from_user.id == config_dict["admin_id"]:
        """logic for change json data"""
        await message.answer("You are admin")

    else:
        await message.answer("You do not have rights to change settings")
