import random
import time

phvar = 0
while phvar == 0:
    N = int(input("Welcome to my Python wordlist generator! Made with <3 by WilliamAfton-codes\nHow long would you like each string to be?: "))
    strings = input("How many strings would you like to generate and add to wordlist.txt?: ")
    for i in range(int(strings)):
        ran_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=N)) + '\n'
        fo = open('wordlist.txt', 'a')
        fo.seek(0)
        fo.writelines(ran_str)
        print(ran_str)
        time.sleep(0.5)
    I2 = input('Would you like to generate more? (y/n): ').lower()
    if I2 == 'n':
        print("Okay, closing.\n")
        input("[Press Enter to exit.]")
        phvar += 1
        break
    elif I2 == 'y':
        pass
