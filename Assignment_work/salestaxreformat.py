#Ask the user on what product they would like to list their
#product for and how much they are selling it for
#by listing it on our site





def main():
    #ask user for merchandise information
    ask_user_for_merchandise = input('Please enter the sellers merchandise name: ')
    ask_user_for_purchase = float(input('What is the dollar amount of purchase, for '
                                        + ask_user_for_merchandise + '\n'
                                                                     'the seller would like to list it for?: '))
    # merchandise name & amount of purchase
    merchandise_name = ask_user_for_merchandise
    amount_of_purchase = ask_user_for_purchase
    #county and states tax
    county_tax = .025
    state_tax = .05



#purchase information
def county_tax_information(merchandise_name,amount_of_purchase,county_tax):
#inputing taxes from both state and county,
#including the combined tax
#and total bill
    tax = county_tax *(merchandise_name, amount_of_purchase)

def state_tax_information(merchandise_name,amount_of_purchase,state_tax, tax):
    st_tax = state_tax * amount_of_purchase
    combined_tax = state_tax + tax
    total_bill = combined_tax + amount_of_purchase
    #result



def results():
    print('')
    print(county_tax_information())
    print('The Amount of Purchase is: $', round(amount_of_purchase))
    print('County and state taxes are included for ', merchandise_name)
    print('County tax is: $', round(county_tax))
    print('State tax is: $', round(state_tax))
    print('Combined tax is: $',round(combined_tax))
    print('Total Bill is: $', round(total_bill))
    input('Thank you for using sales tax app, please press' + '\n'
          + 'Enter, to exit')

#End of Program
#Made by Jonathan Almawi

