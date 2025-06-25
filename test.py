import os
import random

yeslist = ["y", "Y", "yes", "Yes","Yes"]
choicehorcelist = ["1", "2", "3", "4", "5", "6"]
horcenamelist = ["ブレイブハート", "ウィナーズラン", "スピードスター", "ロングラン", "フューチャー", "エンジェル"]
ranking_pre = []

class horce:
    def __init__(self, horce_num:int):
        self.num = horce_num
        self.name = horcenamelist[horce_num - 1]
        self.speed = random.randint(70, 100)
        if self.speed > 85:
            self.stamina = random.randint(50, random.randint(70, 90))
            if self.speed > 95:
                self.stamina = random.randint(45, random.randint(50, 80))
        else:
            self.stamina = random.randint(60, random.randint(70, 100))
        self.luck = random.randint(60, 100)
        self.tech = random.randint(60, 100)
        self.weather = random.randint(0, 2)
        self.pos = 0

    def run_one(self):
        randseed = random.randint(0, 100)#100 change task
        if self.stamina < randseed:
            self.pos = self.pos + self.speed*1.4
        elif self.stamina/2 < randseed:
            self.pos = self.pos + self.speed
        else:
            self.pos = self.pos + self.speed*0.8


class ticket(horce):

    def __init__(self, one, two, three, four, five, six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def run_all(self, moveway:int, horce1:horce, horce2:horce, horce3:horce, horce4:horce, horce5:horce, horce6:horce):
        horce1.run_one()
        



def check_status(horce1:horce, horce2:horce, horce3:horce, horce4:horce, horce5:horce, horce6:horce):
    print(horce1.name, " horcenum:", horce1.num, " speed:", horce1.speed, " stamina:", horce1.stamina, " luck:", horce1.luck, " technic", horce1.tech, "\n")
    print(horce2.name, " horcenum:", horce2.num, " speed:", horce2.speed, " stamina:", horce2.stamina, " luck:", horce2.luck, " technic", horce2.tech, "\n")
    print(horce3.name, " horcenum:", horce3.num, " speed:", horce3.speed, " stamina:", horce3.stamina, " luck:", horce3.luck, " technic", horce3.tech, "\n")
    print(horce4.name, " horcenum:", horce4.num, " speed:", horce4.speed, " stamina:", horce4.stamina, " luck:", horce4.luck, " technic", horce4.tech, "\n")
    print(horce5.name, " horcenum:", horce5.num, " speed:", horce5.speed, " stamina:", horce5.stamina, " luck:", horce5.luck, " technic", horce5.tech, "\n")
    print(horce6.name, " horcenum:", horce6.num, " speed:", horce6.speed, " stamina:", horce6.stamina, " luck:", horce6.luck, " technic", horce6.tech, "\n")
    input("Press Enter Key")
    menu()

horceticket = None

def buy_ticket():
    global horceticket
    global ranking_pre
    if (horceticket != None):
        if (input("Buy a new ticket? Y/N:") not in yeslist):
            menu()
    print("please horcenum 1～6")
    ranking_pre = []
    for i in range(6):
        num = input(f"\n{i}st?:")
        try:
            int(num)
        except Exception:
            print("please 1～6")
            i = i - 1
            continue
        if num in ranking_pre:
            print("already exists")
            i = i - 1
            continue
        elif num not in range(6):
            print("please 1～6")
            i = i - 1
            continue
        elif num in range(6):
            ranking_pre.append(int(num))
    

def menu():
    # set horce
    horce1 = horce(1)
    horce2 = horce(2)
    horce3 = horce(3)
    horce4 = horce(4)
    horce5 = horce(5)
    horce6 = horce(6)

    print("Menu!\n")
    print("################\n")
    print("1.Start to race!\n")
    print("2.Buy a ticket\n")
    print("3.Check status\n")
    print("################\n\n\n")
    selectnum = input("Please number:")

    if selectnum == "1":
        return
    elif selectnum == "2":
        buy_ticket()
    elif selectnum == "3":
        check_status(horce1, horce2, horce3, horce4, horce5, horce6)
    else:
        return

def main():
    print("Welcome to rk01m's horce racing!\n\n\n")
    startmenu = input("Go to menu y/n:")
    if startmenu in yeslist:
        menu()
    else:
        print("Good bye!\nPress Enter Key...")
        input()
    return

if __name__ == "__main__":
    main()