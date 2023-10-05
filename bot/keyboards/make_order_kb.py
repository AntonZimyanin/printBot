from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_online_order_kb(make_order_button: bool = False) -> ReplyKeyboardMarkup:
    '''
    get online order keyboard
    with button 
    Cделать заказ and Отменить заказ
    '''
    kb = [
        [
            KeyboardButton(text="Отменить заказ")
        ],
    ]
    if make_order_button: 
        kb.insert(0, [
            KeyboardButton(text="Cделать заказ")
        ])

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    return keyboard