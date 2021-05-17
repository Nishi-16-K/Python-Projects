import random

def guess(x):
     random_num = random.randint(1, 10)
     guess = 0
     while guess != random_num:
         guess = int(input("Guess a number between 1 and 10: "))
         if guess < random_num:
             print('Sorry, guess again. The number is too low.')
         elif guess > random_num:
            print('Sorry, guess again. The number is too high.')
     print("Hurray! congrats. You've guessed the number correctly")
     
guess(10)
