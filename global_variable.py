myValue = int(input('Enter a number to be \n' +
                    'a global variable ' ))

#Never use global variable security risk, only use it if you want a constant
#like pi, tax rate, etc stuff that doesnt change or doesnt change for a long time
#HOwever it adds complexity to your program, all your subsystems depends on that 'global variable'

def showValue():
    print(myValue)


def main():
    global myValue
    myValue = 9
    showValue()

showValue()
main()