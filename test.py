from tools import *

with open(config['DB']['support'], mode = "r", encoding="utf-8") as fl:
    sup_id = json.load(fl)

if __name__ == "__main__":
    for i in range(5):
        a = Supports_DB()
        print(sup_id["telegram_id"]["client_id"])
