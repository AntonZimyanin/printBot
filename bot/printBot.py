from aiogram import Router
from aiogram.filters import CommandStart    
from aiogram.types import Message    
from aiogram import F
from aiogram import Bot

from bot.config_data import config_data

config_dict = config_data("bot/config.json")


bot = Bot(config_dict["bot_token"])

router = Router(name="print_router")


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
            """Welcome to the prinBot""",
        )
    

@router.message(F.text.contains("печат"))
async def print_filter(message: Message):

#     if message.text in ("Кто печатает?",
#      "Кто распечатает?",
#      "Кто может распечатать?",
#     ):
#         message.answer(f"""
# Если нужно распечатать обращайтесть к ней:
# {config_dict["manager_name"]}                       
# """)

    await bot.send_message(chat_id=config_dict["admin_id"], text="check group")
    await bot.send_message(chat_id=config_dict["manager_id"], text="check group")

    
  
    

    

