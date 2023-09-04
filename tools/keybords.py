from settings import *

class Start_KYB:
    def __init__(self, msg_id) -> None:    
        start_chating = types.InlineKeyboardMarkup()
        start_sup = types.InlineKeyboardButton(text="Начать сеанс", callback_data="Start." + msg_id)
        start_chating.add(start_sup)