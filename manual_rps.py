import random

rps_list = ['rock', 'paper', 'scissors']

def get_computer_choice():
    rps_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(rps_choices)
    return computer_choice

def get_user_choice():
    rps_choices = ['Rock', 'Paper', 'Scissors']
    while True:
        user_choice = input("User Choice: Rock, Paper or Scissors? >> ").title()
        if user_choice in rps_choices:
            return user_choice
        else:
            print('Invalid input. Please enter either rock, paper or scissors. Input is not case sensitive.')

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return f'It is a tie!'
    elif (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        return f'You lost'
    else:
        return f'You won!'

print(get_winner('Rock', 'Paper'))
print(get_winner('Paper', 'Rock'))
print(get_winner('Rock', 'Scissors'))
print(get_winner('Scissors', 'Paper'))
print(get_winner('Paper', 'Paper'))
print(get_winner('Paper', 'Scissors'))



