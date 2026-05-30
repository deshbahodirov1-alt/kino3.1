from aiogram.fsm.state import State, StatesGroup


class AddMovie(StatesGroup):
    waiting_for_name = State()
    waiting_for_language = State()
    waiting_for_genre = State()

class AddGroup(StatesGroup):
    waiting_for_name = State()
    waiting_for_url = State()