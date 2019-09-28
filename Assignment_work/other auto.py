
loan_payment = float(input('How much is your loan? $'))
insurance_payment = float(input('How much is your insurance? $'))
gas_payment = float(input('How much is your gas? $'))
tires_payment = float(input('How much is your tires? $'))
maintence_payment = float(input('How much is your maintence? $'))

def main(loan_payment,insurance_payment, gas_payment, tires_payment, maintence_payment):
    total = loan_payment + insurance_payment + gas_payment + tires_payment + maintence_payment
    print('Your total cost is $',total)


main(loan_payment,insurance_payment, gas_payment, tires_payment, maintence_payment)