from aiogram import Router,types

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import reply_markup_union
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.repaykeyboard.kiyimkeyboards import b_sport,b_klasic,b_oversize,b_uy,b_type,b_rang
from states.kiyimlarstates import KiyimlarState
router = Router()



