def find_prime_1(primenum:int):
    for target_num in range(primenum):
        for i in range(target_num):
            if target_num == i+2: print(target_num)
            if target_num % (i+2) == 0: break


def find_prime_2(primenum:int):
    target_num = 0
    count = 0
    while count != primenum:
        i = 0
        while i != target_num:
            if target_num == i+2:
                print(target_num)
                count = count+1
            if target_num % (i+2) == 0:break
            i = i+1
        target_num = target_num+1

def main():
    if input("mode 1or2\n") == "1":
        find_prime_1(int(input("plz num\n")))
    else:
        find_prime_2(int(input("plz num\n")))

main()