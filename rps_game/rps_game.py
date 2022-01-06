import random

arr = ['rock', 'paper', 'scissors']

user_input = input(f"what's yours_choice --> 'rock', 'paper' or 'scissors'? ").lower()
computer_input = random.choice(arr)


if user_input == 'rock' or user_input == 'paper' or user_input == 'scissors':
        
    if computer_input == user_input:
        print(f'computer-{computer_input}\nyours_choice-{user_input}\n------------------------\nTied')

    if computer_input=='rock' and user_input=='paper':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Won')
    elif computer_input=='paper' and user_input=='rock':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Lost')

    if computer_input=='scissors' and user_input=='rock':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Won')
    elif computer_input=='rock' and user_input=='scissors':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Lost')

    if computer_input=='paper' and user_input=='scissors':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Won')
    elif computer_input=='scissors' and user_input=='paper':
        print(f'computer-->{computer_input}\nyours_choice-->{user_input}\n------------------------\nYou Lost')
else:
    print(f"Plese choose either of these options 'rock', 'paper' or 'scissors'")