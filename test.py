import os
import random

class horce:
    def __init__(self, horce_name=None):
        self.horce_name = str(horce_name)
        self.speed = random.randint(70, 100)
        if self.speed > 85:
            self.stamina = random.randint(50, random.randint(70, 90))
            if self.speed > 95:
                self.stamina = random.randint(45, random.randint(50, 80))
        else:
            self.stamina = random.randint(60, random.randint(70, 100))
        self.luck = random.randint(60, 100)
        self.pos = 0

    def run_horce(self):
        randseed = random.randint(0, 100)#100 change task
        if self.stamina < randseed:
            self.pos = self.pos + self.speed*1.4
        elif self.stamina/2 < randseed:
            self.pos = self.pos + self.speed
        else:
            self.pos = self.pos + self.speed*0.8

class ticket:

    def __init__(self, 1st, 2st, 3st, 4st, 5st, 6st):
        self.1st = 1st
        self.2st = 2st
        self.3st = 3st
        self.4st = 4st
        self.5st = 5st
        self.6st = 6st

def check_status()

def menu():
    # set horce
    horce1 = horce()
    horce2 = horce()
    horce3 = horce()
    horce4 = horce()
    horce5 = horce()
    horce6 = horce()

    print("Menu!\n")
    print("################\n")
    print("1.Start to race!\n")
    print("2.Buy a ticket\n")
    print("3.Check status\n")
    print("4.Change horce name\n")
    print("################\n\n\n")
    selectnum = puts("Please number:")

    if selectnum == "1":

    elif selectnum == "2":

    elif selectnum == "3":
        check_status
    elif selectnum == "4":
    else:

def main():
    print("Welcome to rk01m's horce racing!\n\n\n")
    startmenu = puts("Go to menu y/n:")
    if startQ == ("y" or "Y" or "yes" or "Yes" or "Yes")
        menu()
    else:
        print("Good bye!\nPress Enter Key...")
        puts()
    return

if __name__ == "__main__":
    main()