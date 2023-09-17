from aiogram import Bot
from aiogram import F
from aiogram import Router

from bot.config_data import config_dict


bot = Bot(config_dict["bot_token"])

router = Router(name="print_router")


@router.message(F.text.lower().contains("печат"))
async def print_filter():

    await bot.send_message(chat_id=config_dict["admin_id"], text="check group")
    # await bot.send_message(chat_id=config_dict["manager_id"], text="check group")
