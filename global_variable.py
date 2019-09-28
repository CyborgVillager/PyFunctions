myValue = int(input('Enter a number to be \n' +
                    'a global variable ' ))

#Never use global variable security risk, only use it if you want a constant
#like pi, tax rate, etc stuff that doesnt change or doesnt change for a long time
#HOwever it adds complexity to your program, all your subsystems depends on that 'global variable'
#more use of this will create spageti code
#global constant on the other hand is a good thing like myValue=10


#functions
def showValue():
    print(myValue)


def main():
    global myValue
    myValue = 9
    showValue()

def connect_function():
    print('\n')
    print('connect function result:')
    main()
    showValue()



#result
showValue()
main()
connect_function()
