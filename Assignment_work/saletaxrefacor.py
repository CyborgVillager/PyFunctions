#reformat sales tax to include functions chap 5 pg 229


def ask_user_for_purchase():
    # ask user for merchandise information

    ask_user_for_purchase = float(input('What is the dollar amount of purchase, for '))

    #once system has the amount return it
    return ask_user_for_purchase
#
def state_tax_calc( ask_user_for_purchase ):
    #create a var and calc the user input
    state_tax = .05 * ask_user_for_purchase
    return state_tax

def county_tax( ask_user_for_purchase ):
    county_tax = .025 * ask_user_for_purchase
    return county_tax

                    #could be any var for the function
def total_tax_calc(state_tax, county_tax ):
    total_tax = state_tax + county_tax
    return total_tax

def total_bill(ask_user_for_purchase, total_tax):
    total_bill = ask_user_for_purchase + total_tax
    return total_bill

def result_details(user_amount_of_purchase,calculate_state_tax,calculate_county_tax, \
                   calculate_total_tax, cal_total_sale):
    print('The Amount of Purchase is: $', format(user_amount_of_purchase, ',.2f'), \
          'The State Taxt is: $', format(calculate_state_tax, ',.2f'), \
          'The County Tax  is: $', format(calculate_county_tax, ',.2f'), \
          'The total tax is: $', format(calculate_total_tax, ',.2f'), \
          'The total sale is: $', format(cal_total_sale, ',.2f'), sep='\n')






def main():
    user_amount_of_purchase = ask_user_for_purchase()
    calculate_state_tax = state_tax_calc(str(ask_user_for_purchase))
    calculate_county_tax = county_tax(str(ask_user_for_purchase ))
    calculate_total_tax = total_tax_calc(calculate_state_tax, calculate_county_tax)
    cal_total_sale = total_bill(user_amount_of_purchase,calculate_total_tax)
    result_details(user_amount_of_purchase,calculate_state_tax,calculate_county_tax, \
                   calculate_total_tax, cal_total_sale)





main()
