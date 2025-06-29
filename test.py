import os
import random

yeslist = ["y", "Y", "yes", "Yes","Yes"]
choicehorselist = ["1", "2", "3", "4", "5", "6"]
horsenamelist = horse_names = ["ブレイブハート", "ウィナーズラン", "スピードスター", "ロングラン　　", "フューチャー　", "エンジェル　　",
                                "ゴールデンサン", "ドリームクロス", "ミラクルギフト", "スターライト　", "シルバーホース", "ビクトリーワン",
                                "アースクエイク", "レジェンダー　", "シャイニング　", "プラチナムーン", "スカイハイ　　", "ワンダーホース",
                                "ハヤブサ　　　", "ファントム　　", "ジェネシス　　", "コズミック　　", "サンライズ　　", "ナイトメア　　",
                                "オリオン　　　", "フェニックス　", "ペガサス　　　", "ユニコーン　　", "ドラゴン　　　", "ノーブルホース",
                                "シルバーウルフ", "エメラルキング", "ルビーロード　", "クリスタルマン", "アイアンホース", "ブロンズナイト",
                                "スチールハート", "チタンブレード", "サンダーボルト", "レインボゲート", "エコオブタイム", "サイレントマン", 
                                "マジックアワー", "ファーストスタ", "ラストチャンス", "ヒドゥンフォー", "トゥルービジョ", "ノブルプリンス"
]
horseticket = []
horselist = []


class horse:
    def __init__(self, horse_name:str, num):
        self.name = horse_name
        self.num = num
        self.speed = random.randint(60, 100)

        if self.speed > 80:
            self.stamina = random.randint(50, random.randint(70, 90))
            if self.speed > 90:
                self.stamina = random.randint(45, random.randint(50, 80))
        else:
            self.stamina = random.randint(60, random.randint(70, 100))

        self.tech = random.randint(60, 100)

        self.weather = random.randint(0, 2)

        self.luck = random.randint(60, 100)

        self.pos = 0

    def run_one(self):
        randseed = random.randint(0, 100)#100 change task
        if self.stamina < randseed:
            self.pos = self.pos + self.speed*1.3
        elif self.stamina/2 < randseed:
            self.pos = self.pos + self.speed
        else:
            self.pos = self.pos + self.speed*0.8

class stadium:

    def __init__(self):
        if random.randint(0, 2) == 2:
            self.weather = "cloudy"
        else:
            self.weather = "sunny"

        self.cource = random.randint(12500, 17000)
        self.line = random.randint(75000, 10000)
        self.curve = random.randint(self.cource - self.curve, self.cource)


def run_all():
    global coin
    global bet_coin

    for i in range(6):
        horselist[i].pos = 0
    for i in range(100):
        for i in range(6):
            horselist[i].run_one()
    ranking_list = []
    for i in range(6):
        ranking_list.append((horselist[i].pos, horselist[i].num, horselist[i].name))
    ranking_list = sorted(ranking_list, reverse=True, key=lambda item : item[0])
    rankingnum_list = []
    for i in range(len(ranking_list)):
        print(f"{i+1}st:",f"{str(ranking_list[i][1])}:{ranking_list[i][2]}")
        rankingnum_list.append(int(ranking_list[i][1]))
    if rankingnum_list == horseticket:
        print("YOU ARE SUPERSTAR!!!!!!!!!\nreturn coin x150!")
        coin = coin + int(bet_coin) * 149
        menu()
    returncoin = [50, 20, 8, 3, 1.5]
    for i in range(5):
        if rankingnum_list[i] == horseticket[i]:
            print(f"YOU ARE NICE!!!\nreturn coin x{returncoin[i]}")
            coin = round(coin + int(bet_coin) * returncoin[i])
            menu()

    for i in range(5):
        if i == 0:
            if rankingnum_list[i] == horseticket[i+1]:
                print(f"YOU ARE GOOD\nreturn coin x0.3")
                coin = round(coin - int(bet_coin) * 0.7)
                menu()
                
        elif i == 5:
            if rankingnum_list[i] == horseticket[i-1]:
                print(f"YOU ARE GOOD\nreturn coin x0.3")
                coin = round(coin - int(bet_coin) * 0.7)
                menu()
        else:
            if rankingnum_list[i] == horseticket[i+1] or ranking_list[i] == horseticket[i-1]:
                print(f"YOU ARE GOOD\nreturn coin x0.3")
                coin = round(coin - int(bet_coin) * 0.7)
                menu()

    for i in range(5):
        if i == 0 or i == 1:
            if rankingnum_list[i] == horseticket[i+2]:
                print(f"YOU ARE GOOD\nreturn coin x0.1")
                coin = round(coin - int(bet_coin) * 0.9)
                menu()
                
        elif i == 5 or i == 4:
            if rankingnum_list[i] == horseticket[i-2]:
                print(f"YOU ARE GOOD\nreturn coin x0.1")
                coin = round(coin - int(bet_coin) * 0.9)
                menu()
        else:
            if rankingnum_list[i] == horseticket[i+2] or ranking_list[i] == horseticket[i-2]:
                print(f"YOU ARE GOOD\nreturn coin x0.1")
                coin = round(coin - int(bet_coin) * 0.9)
                menu()


    print("YOU ARE GOOD\nreturn coin x0.01")
    coin = round(coin - int(bet_coin) * 0.99)

    menu()




def check_status():
    for i in range(6):
        print(horselist[i].name, " horsenum:", horselist[i].num, " speed:", horselist[i].speed, " stamina:", horselist[i].stamina, " luck:", horselist[i].luck, " technic", horselist[i].tech)
    input("Press Enter Key")
    menu()


def buy_ticket():
    global horseticket
    global ranking_pre
    global bet_coin
    if (horseticket != []):
        if (input("Buy a new ticket? Y/N:") not in yeslist):
            menu()
    bet_coin = input("How many coins to bet")
    try:
        int(bet_coin)
    except Exception:
        print("please int")
        menu()
    if int(bet_coin) > coin:
        print("huge")
        menu()
    elif input(f"{bet_coin}:bet OK? Y/N\n") not in yeslist:
        print("OK")
        menu()

    print("please horsenum 1~6")
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
        print(f"{i + 1}st:horsenum is {ranking_pre[int(i)]}")
    if input("Do you buy This ticket? Y/N:") not in yeslist:
        buy_ticket()
    horseticket = ranking_pre
    menu()


def menu():

    print("Menu!\n")
    print("coin:", coin)
    print("################")
    print("1.Start to race!")
    print("2.Buy a ticket")
    print("3.Check status")
    print("4.Exit or change horse")
    print("################\n\n")
    selectnum = input("Please number:")

    if selectnum == "1":
        if horseticket == []:
            print("please buy ticket")
            menu()
        else:
            print("Is this OK?")
            for i in range(len(horseticket)):
                print(f"{i+1}st", horseticket[i])
            if input("Y/N:") in yeslist:
                run_all()
            else:
                input("Let's buy!")
                menu()

    elif selectnum == "2":
        buy_ticket()
    elif selectnum == "3":
        check_status()
    elif selectnum == "4":
        main()
    else:
        print("please 1~3")

def main():
    global horselist
    horselist = []
    global coin
    coin = 30000

    #set horse
    horsenamelist_copy = horsenamelist
    for i in range(6):
        horse_num = random.randint(0, len(horsenamelist_copy) - 1)
        horselist.append(horse(horsenamelist_copy[horse_num], i+1))
        horsenamelist_copy.pop(horse_num)

    print("Welcome to rk01m's horse racing!\n\n")
    startmenu = input("Go to menu Y/N:")
    if startmenu in yeslist:
        menu()
    else:
        print("Good bye!\nPress Enter Key...")
        input()
    return

if __name__ == "__main__":
    main()