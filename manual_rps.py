import random

rps_list = ['rock', 'paper', 'scissors']

def get_computer_choice():
    rps_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(rps_choices)
    return computer_choice

def get_user_choice():
    rps_choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Player 1: Rock, Paper or Scissors? >> ").lower()
        if user_choice in rps_choices:
            return user_choice
        else:
            print('Invalid input. Please enter either rock, paper or scissors. Input is not case sensitive.')


print(get_user_choice())
print(get_computer_choice())

