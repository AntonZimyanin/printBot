from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from bot.config_data import config_dict


def get_user_kb() -> InlineKeyboardMarkup: 

    buttons = [
        [
            InlineKeyboardButton(
                    text="В каком блоке печатают?",
                    callback_data="В каком блоке печатают?"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="Цена печати одного листа",
                    callback_data="Цена печати одного листа"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="Свой вопрос",
                    callback_data="Свой вопрос", 
                    url=f"tg://user?id={config_dict['manager_id']}"
                    )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard

