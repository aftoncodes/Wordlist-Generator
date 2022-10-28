import random
import time

print("Welcome to my Python wordlist generator! Made with <3 by WilliamAfton-codes")    # Welcome message
var = 0     # Sets loop variable so that if I2 is 'n' it will end ALL loops
while var == 0:     # Begins whole loop
    N = int(input("How long would you like each string to be?: "))      # Asks how long each word will be
    strings = input("How many strings would you like to generate and add to wordlist.txt?: ")       # Asks how many words to make
    for i in range(int(strings)):   # Makes the strings and writes them to 'wordlist.txt'
        ran_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=N)) + '\n'
        fo = open('wordlist.txt', 'a')
        fo.seek(0)
        fo.writelines(ran_str)
        print(ran_str)
        time.sleep(0.5)
    while True:     # Once all requested words have been generated, will ask if the user wants to make more
        I2 = input('Would you like to generate more? (y/n): ').lower()
        if I2 == 'n':
            print("Okay, closing.\n")
            input("[Press Enter to exit]")
            var = 1
            break
        elif I2 == 'y':
            break
        else:
            print("Error, please type either y or n to make a selection")
