from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from bot.config_data import config_dict


def get_start_kb() -> InlineKeyboardMarkup: 
    buttons = [
        [
            InlineKeyboardButton(
                    text="\U00002753 FAQ, Общая информация: цена печати...",
                    callback_data="Общая информация"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="\U0001F4E6 Сделать онлайн-заказ",
                    callback_data="Сделать онлайн-заказ"
                    )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_user_kb() -> InlineKeyboardMarkup: 

    buttons = [
        [
            InlineKeyboardButton(
                    text="\U0001F50D В каком блоке печатают?",
                    callback_data="В каком блоке печатают?"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="\U0001F4B8 Цена печати одного листа",
                    callback_data="Цена печати одного листа"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="\U0001F4C0 Можно ли прийти с флешкой?",
                    callback_data="Можно ли прийти с флешкой?"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="\U00002753 Свой вопрос",
                    callback_data="Свой вопрос", 
                    url=f"tg://user?id={config_dict['manager_id']}"
                    )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard

