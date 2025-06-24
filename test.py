import os
import random

class horce:
    def __init__(self, horce_name):
        self.name = "horce" + str(horce_name)
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

    def __init__(self, one, two, three, four, five, six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

def check_status(horce1, horce2, horce3, horce4, horce5, horce6):
    print(horce1.name, " speed:", horce1.speed, " stamina:", horce1.stamina, " luck:", horce1.luck, "\n")
    print(horce2.name, " speed:", horce2.speed, " stamina:", horce2.stamina, " luck:", horce2.luck, "\n")
    print(horce3.name, " speed:", horce3.speed, " stamina:", horce3.stamina, " luck:", horce3.luck, "\n")
    print(horce4.name, " speed:", horce4.speed, " stamina:", horce4.stamina, " luck:", horce4.luck, "\n")
    print(horce5.name, " speed:", horce5.speed, " stamina:", horce5.stamina, " luck:", horce5.luck, "\n")
    print(horce6.name, " speed:", horce6.speed, " stamina:", horce6.stamina, " luck:", horce6.luck, "\n")


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
    print("4.Change horce name\n")
    print("################\n\n\n")
    selectnum = input("Please number:")

    if selectnum == "1":
        return
    elif selectnum == "2":
        print(horce1.stamina)
    elif selectnum == "3":
        check_status(horce1, horce2, horce3, horce4, horce5, horce6)
    elif selectnum == "4":
        return
    else:
        return

def main():
    print("Welcome to rk01m's horce racing!\n\n\n")
    startmenu = input("Go to menu y/n:")
    if startmenu in ["y", "Y", "yes", "Yes","Yes"]:
        menu()
    else:
        print("Good bye!\nPress Enter Key...")
        input()
    return

if __name__ == "__main__":
    main()