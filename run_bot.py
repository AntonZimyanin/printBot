import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from bot import change_settings
from bot import check_print
from bot import user_bot
from bot import online_order
from bot import commands_answer
from bot.bot_object import bot
from bot.filters.chat_type import ChatTypeFilter
from bot.commands import set_bot_commands


async def main(bot: Bot):

    asyncio.get_running_loop()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()

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


    await set_bot_commands(bot=bot)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main(bot=check_print.bot))
