from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.enums.chat_type import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.chat import Chat

from bot.config_data import config_data


config_dict = config_data("bot/config.json")


bot = Bot(config_dict["bot_token"])

router = Router(name="print_router")


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        """Welcome to the prinBot""",
    )


@router.message(
    (F.text.contains("печат") | F.text.contains("Печат")) & Chat.type == ChatType.GROUP
)
async def print_filter(message: Message):

    await bot.send_message(chat_id=config_dict["admin_id"], text="check group")
    # await bot.send_message(chat_id=config_dict["manager_id"], text="check group")
