import asyncio
import logging
from enum import Enum

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from pydantic import BaseModel
from pydantic import RedisDsn

from bot import change_settings
from bot import check_print
from bot import user_bot
from bot import online_order
from bot import commands_answer
from bot.filters.chat_type import ChatTypeFilter
from bot.commands import set_bot_commands
from bot.config_data import config_dict


class FSMMode(str, Enum): 
    MEMORY = "memory"
    REDIS = "redis"


class Redis(BaseModel): 
    dsn: RedisDsn
    fsm_db_int: int
    data_db_id: int


async def main():

    asyncio.get_running_loop()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    if config_dict["fsm_mode"] == FSMMode.MEMORY:
        storage = MemoryStorage()
    else:
        storage = RedisStorage.from_url(
            url=f"{config_dict['redis_dsn']}/{config_dict['redis_fsm_db_id']}",
            connection_kwargs={"decode_responses": True},
        )
    
    dp = Dispatcher(storage=storage)
    bot = Bot(config_dict["bot_token"], parse_mode="HTML")

    check_print.router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))
    user_bot.router.message.filter(ChatTypeFilter(chat_type=["private"]))
    change_settings.router.message.filter(ChatTypeFilter(chat_type=["private"]))
    online_order.router.message.filter(ChatTypeFilter(chat_type=["private"]))
    commands_answer.router.message.filter(ChatTypeFilter(chat_type=["private"]))

    dp.include_router(router=check_print.router)
    dp.include_router(router=change_settings.router)
    dp.include_router(router=user_bot.router)
    dp.include_router(router=online_order.router)
    dp.include_router(router=commands_answer.router)

    try:
        await set_bot_commands(bot=bot)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    except KeyboardInterrupt:
        print("\n^C\n")


if __name__ == "__main__":
    asyncio.run(main())