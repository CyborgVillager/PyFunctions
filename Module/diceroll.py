#This program is just rolling a dice
import random
#Constants for the min and max random numbers

min = 1
max = 6

def main():
    #Create a variable to control the loop
    user_input = 'yes'
    user_input = 'quit'

    #Simulate rolling a dice
    while True:
        user_input = input('type roll to roll your dice!')
        if user_input =='roll' or user_input == 'Roll':
            print('Rolling your dice...')
            print('Your values are": ')
            print(random.randint(min,max))
            print(random.randint(min,max))

        #Do anotyher roll of the dice?
        elif user_input == 'quit' or user_input == 'Quit':
            break
        else:
            user_input = input('Roll the dice again? (type roll, ' + '\n' +
                               ' or type quit 2 times to exit program)')
#            if user_input == 'quit' or user_input == 'Quit':
#               break


#call the main function
main()



