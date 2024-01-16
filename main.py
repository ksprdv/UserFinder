from Host.dnn import Deanon as dnnHost
from Nickname.dnn import Deanon as dnnNick
from Phone.dnn import Deanon as dnnPhone
from colorama import Fore, Style
from time import sleep
from utils import Utils
from os import system as cmd

if __name__ == "__main__":
    #while True:
        cmd("clear")
        Utils.log("Deanon Lite by KasperDEV")
        Utils.log("1 - Номер телефона\n2 - IP\n3 - Никнейм")
        type = input(Utils.text("Выберите тип поиска: "))
        type = int(type)
        cmd("clear")
        if type == 1:
            number = input(Utils.text("Введите номер: "))
            dnnPhone(number).find()
        elif type == 2:
            Ip=input(Utils.text("Введите IP: "))
            dnnHost(Ip).find()
        elif type == 3:
            nick = input(Utils.text("Введите никнейм: "))
            dnnNick(nick).find()
