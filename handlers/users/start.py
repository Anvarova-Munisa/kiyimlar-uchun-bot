from aiogram import Router,types
from aiogram.filters import Command

router = Router()

@router.message(Command("start",prefix="!=-/"))
async def help(message: types.Message):
    n = "  Kiyimlar botiga xhush kelibsiz \n"
    n += "Agar yordam kerak bolsa /help ni bosing"
    await message.answer(n)