#This program converts cups to fluid ounces.

def main():
    #display the intro screen
    # The intro displays an intro screen
    intro()
        #Get the number of cups
    cups_needed = int(input('Enter the number of cups you would like to have: '))
     #Convert the cups to ounces
    cups_to_ounces(cups_needed)

def intro():
    print('This program converts measurments' + '\n'
          + 'in cups to fluid ounces. For your')
    print('reference the formula is: ')
    print('1 cup = 8 fluid ounces')
    print(' ')

    #The cups to ounces funciton accepts a number of
    #cups and displays the quivalent number of ounces.

def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, ' ounces')
    print(' ')

#CAll the main function
main()
