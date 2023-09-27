from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def get_online_order_kb() -> ReplyKeyboardMarkup:
    '''
    get online order keyboard
    with button Cделать заказ
    '''
    kb = [
        [
            KeyboardButton(text="Cделать заказ", ),
        ],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    return keyboard