import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from bot import change_settings
from bot import print_bot
from bot import user_bot
from bot.filters.chat_type import ChatTypeFilter

from aiogram.enums import ChatType


async def main(bot: Bot):

    asyncio.get_running_loop()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()

    print_bot.router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))
    user_bot.router.message.filter(ChatTypeFilter(chat_type=["private"]))
    change_settings.router.message.filter(ChatTypeFilter(chat_type=["private"]))

    dp.include_router(router=print_bot.router)
    dp.include_router(router=change_settings.router)
    dp.include_router(router=user_bot.router)


    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main(bot=print_bot.bot))
