from utils import Utils
import requests

class Deanon:
    def __init__(self, host):
        self.host = host
        
    def find(self):
        try:
            a = requests.get(f"http://ip-api.com/json/{self.host}")
            a = a.json()
            print()
            Utils.log("Страна: "+a["country"])
            Utils.log("Регион: "+a["regionName"])
            Utils.log("Город: "+a["city"])
            Utils.log("Организация: "+a["org"])
            Utils.log("Хост: "+a["query"])
            print()
            Utils.log("Проверка окончена!")
            input()
        except:
            Utils.log("Не удалось проверить Host!")