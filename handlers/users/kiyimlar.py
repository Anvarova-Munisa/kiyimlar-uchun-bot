from aiogram import Router,types

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.repaykeyboard.kiyimkeyboards import b_sport,b_klasic,b_oversize,b_uy,b_type,b_rang
from states.kiyimlarstates import KiyimlarState
router = Router()


@router.message(Command("kiyimlar"))
async def  kiyim(msg: types.Message, state: FSMContext):
    n = "Kiyimlar uchun moljanlangan botga xush kelibsiz!"
    await msg.answer(n, reply_markup=b_type.as_markup(resize_keyboard=True))
    await state.set_state(KiyimlarState.type)



@router.message(KiyimlarState.type)
async def kiyim(msg: types.Message, state: FSMContext):
    text = msg.text

    if "sport" in text:
        keyboards = b_sport
    elif "klasic" in text:
        keyboards = b_klasic
    elif "inamarka" in text:
        keyboards = b_oversize
    elif "uy" in text:
        keyboards = b_uy
    elif "rang" in text:
        keyboards = b_rang
    else:
        await msg.answer("Iltimos, menyudan birini tanlang!")
        return

    await msg.answer(f"{msg.text} kiyimlarni tanlang", reply_markup=keyboards.as_markup())
    await state.update_data(type=msg.text)
    await state.set_state(KiyimlarState.kiyimlar_name)

@router.message(KiyimlarState.kiyimlar_name)
async def kiyim(msg: types.Message, state: FSMContext):
    await state.update_data(kiyimlar_name=msg.text)
    await msg.answer("Mashina rangini kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(KiyimlarState.color)