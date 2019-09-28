#This program demostrates 2 functions that
#have local variables with the same name.

cali_population = 4314525
texas_population = 1502344

def main():
    #call the texas function
    texas()
    #call the calirfornia function
    california()
    #print total popuilation
    total_population(texas_population,cali_population)

def texas():
    input('Please press enter to see texas speech')
    print('HE ya!')
    #have number to add

    print('population for texas is ' + str(texas_population))
    print('')

def california():
    input('Please press enter tos ee california speech')
    print('Mariiujha!')
    # have number to add

    print('population for california is ' + str(cali_population))
    print('')

def total_population(texas_population,cali_population):
    total = texas_population + cali_population
    print('The total population of both states is: ' , total)

main()