#This program displays random numbers
#in the range from 1 - 25
import random


def main():
    enter_number = int(input('Enter a number, max is 150: '))
    number = random.randint(enter_number,150)
    #display the number.
    print('The number is ', number)
    print('')





main()