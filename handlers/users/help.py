from aiogram import Router,types
from aiogram.filters import Command
router = Router()

@router.message(Command("help"))
async def help(msg: types.Message):
    await msg.answer("Bu botdan ozingiz uchun kiyimlar harid qilishingiz mumkun\n"
                     "1) klassik uslubdagi kiyimlar\n"
                     "2) Sport va oversize uslubdagi kiyimlar\n"
                     "3) uyda kiyish uchun moljalangan xar hil turdagi kiyimlar\n\n")