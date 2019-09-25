def divideByPositiveNumber(numerator, denominator):
    if denominator >0:
        return numerator/denominator
    else:
        return -1
total_compensation = float(input('Please enter your total income: '))
hours_worked = int(input('How many hours have you worked? '))

hourlyPay = divideByPositiveNumber(total_compensation, hours_worked)
print('Hourly Pay is $' + str(round(hourlyPay)))