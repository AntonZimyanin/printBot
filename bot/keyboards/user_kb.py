from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from bot.config_data import config_dict


def get_start_kb() -> InlineKeyboardMarkup: 
    buttons = [
        [
            InlineKeyboardButton(
                    text="Общая информация: цена печати, куда идти, с флешкой или без",
                    callback_data="Общая информация"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="Сделать онлайн-заказ",
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
                    text="Можно ли прийти с флешкой?",
                    callback_data="Можно ли прийти с флешкой?"
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

