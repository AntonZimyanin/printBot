from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_print_type_kb() -> InlineKeyboardMarkup: 
    '''
    single-sided or double-sided printing
    '''
    buttons = [
        [
            InlineKeyboardButton(
                    text="Одностороняя",
                    callback_data="Одностороняя"
                    )
        ],
        [
            InlineKeyboardButton(
                    text="Двустороняя",
                    callback_data="Двустороняя"
                    )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard




