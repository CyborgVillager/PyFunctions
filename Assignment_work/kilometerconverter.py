#Kilometer converter
#ask user to enter distance in kilometer then convert that to miles
#conversion formula
#miles = kilometer * .6214

#constant
miles = .6214
tell_user_information = int(input('Enter a number to convert kilometer to miles!'))


def main():
    tell_user_about_math_equation()
    convert_information()


def tell_user_about_math_equation():
    prompt = 'Hello user type any number to convert into kilometers into miles!'


#def convert user input into miles result
def convert_information():
    conversion = tell_user_information * miles
    print('Your kilometer is ', round(conversion), ' in miles!')
    return conversion


main()