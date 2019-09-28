#This program displays step-step instructions
# for dissembling an Acme dryer.
#The main funciton eprform the programs main logic.

def main():
    #Display the start up message
    startup_message()
    input('Press Enter to see Step 1')
    #Display step 1
    step_1()
    input('Press enter to see Step 2')
    # Display step 2
    step_2()
    input('Press Enter to see Step 3')
    #Display step 3
    step_3()
    input('Press Enter to see step 4.')
    step_4()

#The startup_message function displays the
#program initial message on the screen.

def startup_message():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer.')
    print('There are 4 steps in the process.')
    print()
#The step1 funciton displaysx the instructions
#for step 1.
def step_1():
    print('Step 1: Unplug the dryer and ')
    print('move it away from the wall.')
    print()
#The step2 function displays the instructions
#for step2
def step_2():
    print('Step 2: Remove the six screws.')
    print('from the back of the dryer.')
    print()
#The step3 function displays the instructions
#for step 3:
def step_3():
    print('Step 3: Remove the back panel.')
    print('from the dryer.')
    print()
#The step4 function displays the instructions
#for step 4.
def step_4():
    print('Step 4: Pull the top of the')
    print('dryer straight up.')
#Call the main function to begin the program.
main()