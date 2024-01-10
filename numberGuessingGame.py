import random
import math
lower = int(input("Enter lower bound:- "))
# the  input code will take input of user.
upper = int(input("Enter upper bound:-  "))

#generating random number btwn the lower & upper
x = random.randint(lower ,upper)
print("\n\tYou've only",
      round(math.log(upper - lower + 1, 2)), "chances to guess integer! \n")

# initializing the number of guesses
count = 0
# for calc of min number of guesses depending on range
while count < math.log(upper- lower +1,2):
    count += 1
    guess = int(input("Guess a number :- "))
    #condition testing
    if x == guess:
        print("congulations you did it in ", count, "try")
        break
    elif x > guess:
        print("you guessed too small !")
    elif x < guess:
        print("you guessed too high !")    

if count >= math.log(upper - lower + 1, 2):    
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")