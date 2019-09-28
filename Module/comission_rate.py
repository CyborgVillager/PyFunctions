#calcs salesperson pay

def main():
    sales = get_sales()

    #get amt of adv pay
    advanced_pay= get_advanced_pay()

    #determine the commision rate
    commission_rate = determine_commission_rate(sales)

    #calc the pay

    pay = sales * commission_rate - advanced_pay

    #display amount of pay
    print('The pay is $ ', format(pay, ',.2f'), sep='')

    #determine if pay is negative
    if pay < 0:
        print('saleperson must reimburse ' + '\n'
              'the company')
    #the get_sales function gets sales person monthlky sales and return the value

def get_sales():
    #get amount of monthly sales
    monthly_sales = float(input('Enter monthly sales: '))

    #return amount enterted
    return monthly_sales

#the get advance function get the amount of adv pay given rto the sale person / returns that amount
def get_advanced_pay():
    #get amount of adv pay
    print('Enter the amount of adbv pay or')
    print('Press enter 0 if no adv pay was given')
    advanced = float(input('Advanced Pay: '))

    #returns the amount enterted
    return advanced

#dterime comm rate function accepts the
#amount of sales as an argument and returns the
#app commision rate

def determine_commission_rate(sales):
    #determine the commisio rate
    if sales < 10000.00:
        rate = .10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = .12
    elif sales >= 15000.00 and sales <= 17999.99:
        rate = .14
    elif sales >= 18000.00 and sales <= 21999.99:
        rate = .16
    else:
        rate = 1.8
    #return commision rate
    return rate
main()