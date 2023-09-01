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
from time import *


# Стандарт
import re
import configparser

import json
import os

settings_file = "settings"
config = configparser.ConfigParser()
config.read('settings/settings.ini')

def config_update():
    with open(settings_file, 'w') as fl:
        config.write(fl)
    config.read(settings_file)
