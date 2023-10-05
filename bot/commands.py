from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from bot.config_data import config_dict


async def set_bot_commands(bot: Bot):
    usercommands = [
        BotCommand(command="start", description="Комманда запуска бота"),
        BotCommand(command="help", description="Справка по использованию бота"),
        BotCommand(command="faq", description="Частые вопросы"),
        BotCommand(command="online_order", description="Сделать онлайн заказ"),
        BotCommand(command="payment_methods", description="Способы оплаты"),
    ]

    await bot.set_my_commands(usercommands, scope=BotCommandScopeDefault())

    admin_commands = [
        BotCommand(command="change_settings", description="Изменение настроек"),
    ]
    
    await bot.set_my_commands(
        admin_commands,
        scope=BotCommandScopeChat(chat_id=config_dict["admin_id"])
    )