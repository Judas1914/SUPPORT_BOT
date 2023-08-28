from tools import *

if __name__ == "__main__":
    for i in range(5):
        client_db = Client_DB()
        client_db.add(2,"Че???" + str(i))
        client_db.add(1,"Че???" + str(i))