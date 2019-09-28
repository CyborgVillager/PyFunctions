#The following is used as a global constant
#tyhe contribution rate
Contributation_rate = .05

def main():
    gross_pay = float(input('Enter the gross pay:'))
    bonus = float(input('Enter the amount of bonuses: ') )
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

#The show pay_contrib function accepts the gross
#pay as an argument and displays the retirment
#contribuition for the amount of pay.

def show_pay_contrib(gross):
    contrib = gross * Contributation_rate
    print('Contriobution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='')
#The show_bonus function accepts the
#bonus amount as an argument and displays the retirment contirbution for that amount of apy,

def show_bonus_contrib(bonus):
    contrib = bonus * Contributation_rate
    print('Contriobution for bonuos: $', \
          format(contrib, ',.2f'), \
          sep='')

#call the main func
main()