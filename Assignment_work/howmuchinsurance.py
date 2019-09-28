
#global

insurance_cost = float(input('Enter the cost of a building for repair: $'))

def calculate(insurance_cost ):
    insurance = insurance_cost  * 0.8
    print('The minimum amount of insurance you should buy for the property is $', format(insurance, '.2f'))

calculate(insurance_cost )