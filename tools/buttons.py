from .message import *

over = types.InlineKeyboardMarkup()
end_sup = types.InlineKeyboardButton(text="Завершить сеанс", callback_data="end.sup")
over.add(end_sup)