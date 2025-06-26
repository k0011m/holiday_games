import os
import random

yeslist = ["y", "Y", "yes", "Yes","Yes"]
choicehorcelist = ["1", "2", "3", "4", "5", "6"]
horcenamelist = ["ブレイブハート", "ウィナーズラン", "スピードスター", "ロングラン　　", "フューチャー　", "エンジェル　　"]
ranking_pre = []
horceticket = []


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


def run_all():
    for i in range(100):
        horce1.run_one()
        horce2.run_one()
        horce3.run_one()
        horce4.run_one()
        horce5.run_one()
        horce6.run_one()
    ranking_list = [(horce1.pos, f"{horce1.num}:{horce1.name}"), (horce2.pos, f"{horce2.num}:{horce2.name}"), 
                    (horce3.pos, f"{horce3.num}:{horce3.name}"), (horce4.pos, f"{horce4.num}:{horce4.name}"), 
                    (horce5.pos, f"{horce5.num}:{horce5.name}"), (horce6.pos, f"{horce6.num}:{horce6.name}")]
    ranking_list = sorted(ranking_list, reverse=True, key=lambda item : item[0])
    for i in range(len(ranking_list)):
        print(str(ranking_list[i][1]))
    menu()




def check_status(horce1:horce, horce2:horce, horce3:horce, horce4:horce, horce5:horce, horce6:horce):
    print(horce1.name, " horcenum:", horce1.num, " speed:", horce1.speed, " stamina:", horce1.stamina, " luck:", horce1.luck, " technic", horce1.tech)
    print(horce2.name, " horcenum:", horce2.num, " speed:", horce2.speed, " stamina:", horce2.stamina, " luck:", horce2.luck, " technic", horce2.tech)
    print(horce3.name, " horcenum:", horce3.num, " speed:", horce3.speed, " stamina:", horce3.stamina, " luck:", horce3.luck, " technic", horce3.tech)
    print(horce4.name, " horcenum:", horce4.num, " speed:", horce4.speed, " stamina:", horce4.stamina, " luck:", horce4.luck, " technic", horce4.tech)
    print(horce5.name, " horcenum:", horce5.num, " speed:", horce5.speed, " stamina:", horce5.stamina, " luck:", horce5.luck, " technic", horce5.tech)
    print(horce6.name, " horcenum:", horce6.num, " speed:", horce6.speed, " stamina:", horce6.stamina, " luck:", horce6.luck, " technic", horce6.tech)
    input("Press Enter Key")
    menu()


def buy_ticket():
    global horceticket
    global ranking_pre
    if (horceticket != []):
        if (input("Buy a new ticket? Y/N:") not in yeslist):
            menu()
    print("please horcenum 1~6")
    ranking_pre = []
    i = 0
    while i <= 5:
        num = input(f"\n{i + 1}st?:")
        try:
            int(num)
        except Exception:
            print("please 1~6")
            continue
        if int(num) in ranking_pre:
            print("already exists")
            continue
        elif int(num) not in range(7):
            print("please 1~6")
            continue
        elif int(num) == 0:
            print("please 1~6")
            continue
        elif int(num) in range(7):
            i = i + 1
            ranking_pre.append(int(num))
    print("check please\n")
    for i in range(len(ranking_pre)):
        print(f"{i + 1}st:horcenum is {ranking_pre[int(i)]}")
    if input("Do you buy This ticket? Y/N:") not in yeslist:
        buy_ticket()
    horceticket = ranking_pre
    menu()


def menu():
    # set horce

    print("Menu!\n")
    print("################")
    print("1.Start to race!")
    print("2.Buy a ticket")
    print("3.Check status")
    print("################\n\n")
    selectnum = input("Please number:")

    if selectnum == "1":
        if horceticket == []:
            print("please buy ticket")
            menu()
        else:
            print("Is this OK?")
            for i in range(len(horceticket)):
                print(f"{i}st", horceticket[i])
            if input("Y/N:") in yeslist:
                run_all()
            else:
                input("Let's buy!")
                menu()

    elif selectnum == "2":
        buy_ticket()
    elif selectnum == "3":
        check_status(horce1, horce2, horce3, horce4, horce5, horce6)
    else:
        print("please 1~3")

def main():
    global horce1
    global horce2
    global horce3
    global horce4
    global horce5
    global horce6

    horce1 = horce(1)
    horce2 = horce(2)
    horce3 = horce(3)
    horce4 = horce(4)
    horce5 = horce(5)
    horce6 = horce(6)
    print("Welcome to rk01m's horce racing!\n\n\n")
    startmenu = input("Go to menu Y/N:")
    if startmenu in yeslist:
        menu()
    else:
        print("Good bye!\nPress Enter Key...")
        input()
    return

if __name__ == "__main__":
    main()
