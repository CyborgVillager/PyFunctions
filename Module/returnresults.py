


times_total = 0

def main():
    #Get first number
    num0 = int(input('Enter a number: '))

    #Get second number
    num1 = int(input('Enter a second number: '))

    #Get the sum of both number inputs
    sum_total = sum(num0, num1)

    #Display combined numbers
    print('Your inputs add to ', sum_total)


#This returns your input
def sum(num0,num1):
    result = num0 + num1
    return result




#print(sum(total,times))

#print(sum(times))
main()
