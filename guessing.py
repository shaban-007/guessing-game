import random
Actual = random.randrange(1,100)
Guess = 0
while(Actual != Guess):
    x = abs(Actual - Guess)
    Guess = int(input())
    if Guess < 0 or Guess > 100 :
        print ("OUT OF RANGE")
    elif Actual==Guess:
        print("you make it")
        break
    elif abs(Actual - Guess) < x :
        print(' you are closer to target ')
    else :
        print(' you are far from the target ')