#This program displatys 5 random
#numbers in the range of 1 - 150
import random
def main():
    ask_for_number = int(input('Enter a number and it will randomly' + '\n'
                               +'generated 5 numbers! '))
    for count in range(5):
        print(random.randint(1, 150))
#call the main func
main()