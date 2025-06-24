import os
import random

class horce:
    def __init__(self, horce_name="aaa"):
        self.horce_name = str(horce_name)
        self.speed = random.randint(70, 100)
        if self.speed > 85:
            self.stamina = random.randint(50, random.randint(55, 90))
        elif self.speed > 95:
            self.stamina = random.randint(60, random.randint)
        self.luck = random.randint(70, 100)
        self.pos = 0

    def run_horce(self):
        randseed = random.randint(0, 100)
        if self.stamina > randseed:
            self.pos = self.pos + self.speed*1.4
        elif self.stamina /2 > randseed:
            self.pos = self.pos + self.speed
        else:
            self.pos = self.pos + self.speed*0.8
        

def main():
    aaa = horce("hello")
    print(aaa.speed, aaa.stamina, aaa.luck)
    return

if __name__ == "__main__":
    main()