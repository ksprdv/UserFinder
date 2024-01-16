from utils import Utils
import requests

class Deanon:
    def __init__(self, phone):
        self.phonenumber = phone

    def find(self):
        try:
            site_data = requests.post(f'https://htmlweb.ru/json/mnp/phone/{str(self.phonenumber)}')
            data = site_data.json()
            region = data["region"]
            opr = data["oper"]
            print()
            Utils.log("Страна: "+region["country"])
            Utils.log("Регион: "+region["name"])
            Utils.log("Округ: "+ region["okrug"])
            Utils.log("Код машин: "+str(region["autocod"]))
            Utils.log("Оператор: "+opr["name"])
            print()
            Utils.log("Проверка окончена!")
            input()
        except:
            Utils.log("Не удалось проверить номер!")        