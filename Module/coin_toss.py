#This program simulates 10 tosses of a coin
import random
#Constants

Heads = 1
Tails = 2
Tosses = 10
heads_total = 0
tails_total = 0
heads_counter = 0
tails_counter = 0

def main():
    for toss in range(Tosses):
        # Simulates the coin toss.
        if random.randint(Heads,Tails) == Heads:
   #         heads_total = heads_counter + 1
            print('Heads')
        else:
  #          tails_total = tails_counter + 1
            print('Tails')

#   if heads_total > tails_total:
 #       print('Its heads!')
  #  elif heads_total < tails_total:
   #     print('Its tails!')

#call main func
main()
