
yearly_increased = .96

#def house_value():
house_value = float(input('How much would you like to sell this house for?: $'))
#    return house_value


def house_increased(house_value):
    house_increased = yearly_increased * house_value
    return house_increased


def results(house_increased):
    print('The house value is:' + \
          '$', format(house_increased(house_value), '.2f'))
    return results

def main():

    house_increased(house_value)
    results(house_increased)


main()