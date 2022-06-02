# the program to check if user can guess the number Computer generated

# first generate a random number 
import random

gen_number = random.randint(1, 20)

# Users will get 6 chances to guess the number

print("\n *********  Welcome to guess the number game   ********* \n\nYou will get 6 chances to guess the number. \n")
answer = 0
trial = 6

for trials in range(1,7):
    print('\nYou have ' + str(7 - trials) + ' trails left')
    answer = int(input("\nGuess the number between 1 and 20 : "))

    if answer < gen_number:
       print('\nYour guess is lower')
    elif answer > gen_number:
        print('\nYour guess is higher')
    else:
            trial = trials
            break 

if answer == gen_number:
    print('\nYou are a genious. You guessed the number : ' + str(gen_number) + ' correctly in ' + str(trial) + ' trials\n')
else:
    print('Sorry. You lost all your chances. \n The number was: ' + str(gen_number) + '\nBetter luck next time')
         

