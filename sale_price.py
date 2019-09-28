#This program calculates retial items
#sale price

#Discount_percentage is used as global
#constant 4 discount %

discount_percentage = .25

#main func
def main():
    #get item reg $
    reg_price = get_regular_price()

    #calculate the sale price
    sale_price = reg_price - discount(reg_price)

    #display the sale price
    print('the sale price is $ ', format(sale_price, ',.2f'), sep='')

#get_reg_price function promp in
#user enter an item reg price
#return the value
def get_regular_price():
    price = float(input('Enter the items regular price: '))
    return price

#discount function accepts an item price
#as an argument and returns the maount by discount
def discount(price):
    return price * discount_percentage

#call main fun

main()

