import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from bot import change_settings
from bot import printBot
from bot.printBot import bot


async def main(bot: Bot):

    asyncio.get_running_loop()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()

    dp.include_router(router=printBot.router)
    dp.include_router(router=change_settings.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main(bot=bot))
