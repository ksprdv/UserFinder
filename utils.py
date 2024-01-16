from colorama import Fore, Style

class Utils:

    def log(t):
        print(Utils.text(t))

    def text(t):
        return "{}{}{}".format(Fore.WHITE, t, Style.RESET_ALL)