def main():
    value = int(input('Enter a number: '))
    #argument is passed into a function , once it apssed to number is define paremter vairbale
    #their both the same
    show_double(value)


def show_double(number):
    result = number * 2
    print(result)


main()

#the number is assigned the the value
#the value and number are refering to the same piece of data
