from utils import Utils
import requests, colorama,random

class Deanon:
    def __init__(self, nick):
        self.nickname = nick

    def siteList(self):
        print()
        colors = [colorama.Fore.BLUE,colorama.Fore.YELLOW,colorama.Fore.RED,colorama.Fore.GREEN]
        with open("Nickname/sites.txt", "r") as wr:
            sites = wr.readlines()
        new_sites = []
        for site in sites:
            a = site.replace("\n", "")
            if a != "":
                new_sites.append(a)
        return new_sites

    def find(self):
        try:
            sites = self.siteList()
            for st in sites:
                url = st + self.nickname
                try:
                    req = requests.get(url, timeout=2)
                    print(req.status_code)
                    if req:
                        Utils.log("[VALID] " + url)
                    else:
                        Utils.log("[INVALID] " + url)
                except Exception as exc:
                    Utils.log("[INVALID EXCEPTION] " + url)
            print()
            Utils.log("Проверка окончена!")
            input()
        except:
            Utils.log("Не удалось выполнить поиск!")