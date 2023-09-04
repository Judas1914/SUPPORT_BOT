# Для бота
from aiogram import *
from aiogram.dispatcher import Dispatcher
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio


# Стандарт
import re
import configparser
import time
import traceback
import json
import os

settings_file = "settings"
config = configparser.ConfigParser()
config.read('settings/settings.ini')

API_TOKEN = config['Telegram']['token']
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def config_update():
    with open(settings_file, 'w') as fl:
        config.write(fl)
    config.read(settings_file)



####
import logging
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"

)

"""
Места где может произойти ошибка помечай как 
try:
    <блок кода>
except:
    logging.error(traceback.format_exc())
"""