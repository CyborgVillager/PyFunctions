#reformat sales tax to include functions chap 5 pg 229

# ask user for merchandise information
ask_user_for_merchandise = input('Please enter the sellers merchandise name: ')
ask_user_for_purchase = float(input('What is the dollar amount of purchase, for '
                                    + ask_user_for_merchandise + '\n'
                                                                 'the seller would like to list it for?: '))

user_amount_of_purchase = float( input('Please enter amount of purchase: '))

state_tax = .05 * user_amount_of_purchase
county_tax = .025 * user_amount_of_purchase
total_tax = state_tax + county_tax
combined_tax = state_tax + county_tax
total_bill = user_amount_of_purchase + total_tax

print('The Amount of Purchase is: $', round(user_amount_of_purchase))
print('County and state taxes are included for ', ask_user_for_merchandise)
print('County tax is: $', round(county_tax))
print('State tax is: $', round(state_tax))
print('Combined tax is: $', round(combined_tax))
print('Total Bill is: $', round(total_bill))
input('Thank you for using sales tax app, please press' + '\n'
      + 'Enter, to exit')