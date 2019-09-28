#This program uses the return value of a function

def main():
    #Get the user's age
    first_age = int(input('Enter your age: '))

    #Get your brothers age
    second_age = int(input('Enter your sibling age: '))

    #Get the sum of both ages
    total = sum(first_age,second_age)

    #Display total age
    print('together both you are ', total, 'years old!')


# The sum function accepts two numer args and
#returns the sum of those arguments

def sum(first_age, second_age):
    result = first_age + second_age
    return  result

main()