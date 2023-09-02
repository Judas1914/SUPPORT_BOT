from settings import *
from .db import *

API_TOKEN = config['Telegram']['token']
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

with open(config['DB']['support'], mode = "r", encoding="utf-8") as fl:
    sup_id_mas = json.load(fl)

sup_id = sup_id_mas["telegram_id"]["client_id"]
client_id = ""
msg_id_client = []
msg_id_support = []

@dp.message_handler(commands='start')
async def start(message: types.Message):

    with open(config['DB']['support'], mode = "r", encoding="utf-8") as fl:
        sup_id_mas = json.load(fl)

    await bot.send_message(message.chat.id,
                "⚠️Сразу пишите свойю 👉ПОЧТУ (с которой была покупка)\n"
                "👉ЛОГИН аккаунта с которым проблема⚠️\n"
                "И сразу ваш вопрос, если не напишете, то вам и не ответят❗️")

    if sup_id_mas["telegram_id"]["buzy"] == "false":

        start_chating = types.InlineKeyboardMarkup()
        start_sup = types.InlineKeyboardButton(text="Начать сеанс", callback_data="Start." + str(message.chat.id))
        start_chating.add(start_sup)

        await bot.send_message(sup_id,
                        "Вам пишет пользователь"
                        "\nName: " + str(message.chat.first_name) +
                        "\nid: " + str(message.chat.id)
                        ,reply_markup=start_chating)
    else:
        time.sleep(300)

        start_chating = types.InlineKeyboardMarkup()
        start_sup = types.InlineKeyboardButton(text="Начать сеанс", callback_data="Start." + str(message.chat.id))
        start_chating.add(start_sup)

        await bot.send_message(sup_id,
                        "Вам пишет пользователь"
                        "\nName: " + str(message.chat.first_name) +
                        "\nid: " + str(message.chat.id)
                        ,reply_markup=start_chating)


@dp.callback_query_handler(text_contains='Start.')
async def ans(call):
    global client_id, msg_id_client, msg_id_support
    client_id = (call.data.split('.')[1])
    await bot.send_message(client_id, "Поддержка на связи")

    support_db = Supports_DB()
    support_db.buzy("true", sup_id)

    over = types.InlineKeyboardMarkup()
    end_sup = types.InlineKeyboardButton(text="Завершить сеанс", callback_data="end." + str(client_id))
    over.add(end_sup)

    with open(config['DB']['client'], mode = "r", encoding="utf-8") as fl:
        quest = json.load(fl)

    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    await bot.send_message(sup_id,
                        "Начат чат с пользователем"
                        ,reply_markup=over)

    for i in range(len(quest[client_id]["message"])):
        msg = await bot.send_message(sup_id, quest[client_id]["message"][i])
        msg_id_client.append(msg.message_id)


@dp.message_handler(content_types='text')
async def db_add(message: types.Message):
    global client_id, msg_id_client, msg_id_support

    with open(config['DB']['support'], mode = "r", encoding="utf-8") as fl:
        sup_id_mas = json.load(fl)

    with open(config['DB']['client'], mode = "r", encoding="utf-8") as fl:
        quest = json.load(fl)

    if sup_id_mas["telegram_id"]["buzy"] == "true" and str(message.chat.id) != sup_id:

        msg = await bot.send_message(sup_id, message.text)
        msg_id_client.append(msg.message_id)

        client_db = Client_DB()
        client_id = message.chat.id
        client_txt = message.text
        client_db.add(client_id, client_txt)

    elif str(message.chat.id) == sup_id:

        msg = await bot.send_message(client_id, message.text)
        msg_id_support.append(message.message_id)

    else:

        client_db = Client_DB()
        client_id = message.chat.id
        client_txt = message.text
        client_db.add(client_id, client_txt)


@dp.callback_query_handler(text_contains='end.')
async def ans(call):
    global client_id, msg_id_client, msg_id_support
    client_id = (call.data.split('.')[1])

    support_db = Supports_DB()
    support_db.buzy("false", sup_id)

    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    for i in range(len(msg_id_client)):
        await bot.delete_message(chat_id=sup_id, message_id=msg_id_client[i])

    for i in range(len(msg_id_support)):
        await bot.delete_message(chat_id=sup_id, message_id=msg_id_support[i])

    await bot.send_message(client_id,
                        "Сеанс завершон")

    msg_id_client.clear()
    msg_id_support.clear()

    client_db = Client_DB()
    client_db.remove(client_id)

    client_id = ""

