import random

random_num = random.randint(0, 100)

#print(user_guess, type(user_guess))
#print(guess, type(guess))
guess = -1 #se

player_name = input('Enter your name: ')

while guess != random_num:
    user_guess = input('Guess a number between 0 and 100: ')
    guess = int(user_guess)

    if guess < random_num:
        print('Sorry, {}, your guess of {} is too low'.format(player_name, guess))
    elif guess > random_num:
        print('Sorry, {}, your guess of {} is too high'.format(player_name, guess))
    else:
        print('Well done, {}! You win, the number was {}'.format(player_name, guess))
