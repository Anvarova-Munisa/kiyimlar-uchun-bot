from aiogram.fsm.state import State, StatesGroup

class KiyimlarState(StatesGroup):
    type = State()
    kiyimlar_name = State()
    rang = State()
    razmer = State()
    rasm = State()
    info = State()