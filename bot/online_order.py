import asyncio

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from bot.config_data import config_dict
from bot.keyboards.print_type_kb import get_print_type_kb
from bot.keyboards.make_order_kb import get_online_order_kb

from bot.state import File


router = Router(name="online-order")


@router.callback_query(F.data == "Сделать онлайн-заказ")
async def print_type(callback: CallbackQuery):
    await callback.message.edit_text("Выберите тип печати",
      reply_markup=get_print_type_kb()
    )
       

#send print type and username admin and manager
@router.callback_query(F.data.in_({"Одностороняя", "Двустороняя"}) )
async def send_print_type(callback: CallbackQuery, state: FSMContext):
    #user message
    await callback.message.answer("""
Отправьте документ или фото в хорошем качестве
""", reply_markup=get_online_order_kb())

    #admin message
    await callback.bot.send_message(chat_id=config_dict["admin_id"]
                            , text=f"""{callback.data} — @{callback.from_user.username}""")
    
    await state.set_state(File.file)

    await asyncio.sleep(0.5)
    await callback.message.delete()


@router.message(File.file, F.content_type.in_({'document', 'photo'}))
async def send_file(message: Message, state: FSMContext):
    await message.answer("отправлено", reply_markup=get_online_order_kb(make_order_button=True))
    await message.copy_to(chat_id=config_dict["admin_id"])


@router.message(F.text.lower() == "cделать заказ")
async def state_clear(message: Message, state: FSMContext): 
    await message.answer("""
Заказ отправлен, вам напишут, когда его забрать.
""", reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(chat_id=config_dict["admin_id"], text="все")
    await state.clear()


@router.message(F.text.lower() == "отменить заказ")
async def state_clear(message: Message, state: FSMContext):
    await message.answer("""Заказ отменен""", reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(chat_id=config_dict["admin_id"], text="Заказ отменен")
    await state.clear()


@router.message(File.file)
async def dont_send_file(message: Message, state: FSMContext):
    await message.answer("Отправьте, пожалуйста, файл или фото в хорошем качестве")
    
