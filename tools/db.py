# from settings import *

# class Client_DB:
#     def __init__(self):
#         self.__database: dict = self.__load()

#     def __load(self):
#         if os.path.exists(config["DB"]["client"]): # path.exists- проверят существует ли указанный файл в папке True - если файл есть \ False если он отсутсвует
#             with open(config["DB"]["client"], mode = "r", encoding="utf-8") as fl:
#                 data = json.load(fl)
#             return(data)
#         else:
#             data = {}
#             with open(config["DB"]["client"], mode = "w", encoding="utf-8") as fl:
#                 json.dump(data, fl, ensure_ascii=False)
#             return(data)


#     def __update(self):
#         """
#         Обновление базы данных в папке data
#         """
#         with open(config["DB"]["client"], mode = "w", encoding="utf-8") as fl:
#             json.dump(self.__database, fl, ensure_ascii=False)

#     def get_data(self):
#         return self.__database

#     def add(self, id: str, message: str):

#         if str(id) not in list(self.__database.keys()):

#             """Добавление нового пользователя

#             Args:
#                 id (str): ид пользователя
#                 message (str): первое сообщение пользователя
#             """
#             self.__database[str(id)] = {
#                 "buzy": False,
#                 "message": [message] # закидывает полученное сообщение в тип данных списка
#             }
#             self.__update()
#         else:
#             """Дополнение сообщений от существуещего пользователя в БД. Если саппорт ещё не ответил. buzy == False

#             Args:
#                 id (): ид пользователя
#                 message (str): новое сообщение пользователя
#             """
#             self.__database[str(id)]["message"].append(message)
#             self.__update()

#     def remove(self, id):
#         """Удаление клиента по id из базы вопросов

#         Args:
#             id (_type_): ид клиента вопрос которого будет решен
#         """
#         self.__database.pop(str(id))
#         self.__update()


# class Supports_DB:
#     def __init__(self):
#         self.__database = self.__load()

#     def __load(self):
#         if os.path.exists(config["DB"]["support"]):
#             with open(config["DB"]["support"], mode = "r", encoding="utf-8") as fl:
#                 data = json.load(fl)
#             return(data)
#         else:
#             data = {}
#             with open(config["DB"]["support"], mode = "w", encoding="utf-8") as fl:
#                 json.dump(data, fl, ensure_ascii=False)
#             return(data)

#     def get_data(self):
#         return self.__database

#     def __update(self):
#         """
#         Обновление базы данных в папке data
#         """
#         with open(config["DB"]["support"], mode = "w", encoding="utf-8") as fl:
#             json.dump(self.__database, fl, ensure_ascii=False)


#     def buzy(self, buzy: str, id: str):
#         """Смена "занятости"

#         Args:
#             buzy (bool): True or False
#             id (str): поддержки
#         """
#         self.__database["telegram_id"] = {
#             "buzy": buzy,
#             "client_id": id
#         }
#         self.__update()
