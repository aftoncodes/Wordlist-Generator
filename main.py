import threading
import random
import time
import sys

threadnum_arg = 0
strlength_arg = 0
strnum_arg = 0

if len(sys.argv) < 4:
    threadnum_arg = 0
    strlength_arg = 0
    strnum_arg = 0
else:
    threadnum_arg = int(sys.argv[1]) 
    strlength_arg = int(sys.argv[2])
    strnum_arg = int(sys.argv[3])

threadnum = 1
strlength = 10
strnum = 10


def process():
    global threadnum
    global strlength
    global strnum
    global threadnum_arg
    global strlength_arg
    global strnum_arg
    if strnum_arg == 0:
        if strlength_arg == 0:
            for i in range(strnum):
                ran_str = ''.join(
                    random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=strlength)) + '\n'
                fo.seek(0)
                fo.writelines(ran_str)
                print(ran_str)
        else:
            for i in range(strnum_arg):
                ran_str = ''.join(
                    random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=strlength_arg)) + '\n'
                fo.seek(0)
                fo.writelines(ran_str)
                print(ran_str)
    else:
        if strlength_arg == 0:
            for i in range(strnum):
                ran_str = ''.join(
                    random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=strlength)) + '\n'
                fo.seek(0)
                fo.writelines(ran_str)
                print(ran_str)
        else:
            for i in range(strnum_arg):
                ran_str = ''.join(
                    random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=strlength_arg)) + '\n'
                fo.seek(0)
                fo.writelines(ran_str)
                print(ran_str)


if __name__ == "__main__":
    fo = open('wordlist.txt', 'a')

    print("Welcome to my Python wordlist generator! Made with <3 by WilliamAfton-codes")

    if threadnum_arg == 0:
        while True:
            threadnum = input("How many threads would you like to use?: ")
            if threadnum.isdigit():
                if int(threadnum) > 0:
                    break
                else:
                    print("Please enter a number larger than 0!")
            else:
                print("Please input a valid integer!")
                

    if strlength_arg == 0:
        strlength = int(input("How long would you like each string to be?: "))

    if strnum_arg == 0:
        strnum = int(input("How many strings do you want to generate (Each thread will generate the selected amount)?: "))

    if threadnum_arg == 0:
        for i in range(int(threadnum)):
            x = threading.Thread(target=process)
            x.start()
            x.join()
    else:
        for i in range(int(threadnum_arg)):
            x = threading.Thread(target=process)
            x.start()
            x.join()

    input("[Press Enter to exit.]")
