#inputing taxes from both state and county,
#including the combined tax
#and total bill

#This is global info
county_default_tax = .025
state_default_tax = .05



ask_user_for_merchandise = input('Please enter the sellers merchandise name: ')
ask_user_for_cost_amount = float(input('What is the dollar amount of purchase, for '
                                   + ask_user_for_merchandise + '\n'
                                   'the seller would like to list it for?: '))




#calc the tax info
def tax():
    state_tax = ask_user_for_cost_amount * state_default_tax
    county_tax = ask_user_for_cost_amount * county_default_tax
    total_tax = county_tax + state_tax
    total = ask_user_for_cost_amount + total_tax
    print("Your total is $", format(total, ".2f"), '\n',
          'for ', ask_user_for_merchandise )


#main program
def main():
    tax()


#result
main()
