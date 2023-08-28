from settings import *
from .db import *
from .States import *
from .buttons import *

API_TOKEN = config['Telegram']['token']
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                    "⚠️Сразу пишите свойю 👉ПОЧТУ (с которой была покупка)\n"
                    "👉ЛОГИН аккаунта с которым проблема⚠️\n"
                    "И сразу ваш вопрос, если не напишете, то вам и не ответят❗️")

    await Form.chating.set()



@dp.message_handler(state=Form.chating)
async def start(message: types.Message, state: FSMContext):
    client_db = Client_DB()
    client_id = message.chat.id
    client_txt = message.text
    client_db.add(client_id, client_txt)




