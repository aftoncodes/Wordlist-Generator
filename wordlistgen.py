import threading
import random
import time

threadnum = 1
strlength = 10
strnum = 10


def process():
    global threadnum
    global strlength
    global strnum
    for i in range(strnum):
        ran_str = ''.join(
            random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=strlength)) + '\n'
        fo.seek(0)
        fo.writelines(ran_str)
        print(ran_str)


if __name__ == "__main__":
    fo = open('wordlist.txt', 'a')

    print("Welcome to my Python wordlist generator! Made with <3 by WilliamAfton-codes")

    while True:
        threadnum = input("How many threads would you like to use?: ")
        if threadnum.isdigit():
            if int(threadnum) > 0:
                break
            else:
                print("Please enter a number larger than 0!")
        else:
            print("Please input a valid integer!")

    strlength = int(input("How long would you like each string to be?: "))

    strnum = int(input("How many strings do you want to generate (Each thread will generate the selected amount)?: "))

    for i in range(int(threadnum)):
        x = threading.Thread(target=process)
        x.start()
        x.join()

    input("[Press Enter to exit.]")
