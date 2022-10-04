import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    option = ['rock', 'paper', 'scissors']
    user_input = input('Choose rock, paper, scissors or exit: ')
    computer_input = random.choice(option)

    if user_input == 'exit':
        print('Game has ended')
        print('You won a total score of '+user_points+' and the computer total score is'+computer_points)
        exit = True

    if user_input == 'rock':
        if computer_input == 'rock':
            print('Your input is rock')
            print('computer input is rock')
            print('It is a tie!')
        elif computer_input == 'paper':
            print('Your input is rock')
            print('computer input is paper')
            print('computer wins')
            computer_points += 1
        elif computer_input == 'scissors':
            print('Your input is rock')
            print('computer input is scissors')
            print('you wins')
            user_points += 1

    elif user_input == 'paper':
        if user_input == 'rock':
            if computer_input == 'rock':
                print('Your input is paper')
                print('computer input is rock')
                print('You win!')
                user_points += 1
            elif computer_input == 'paper':
                print('Your input is paper')
                print('computer input is paper')
                print('its a tie!')
            elif computer_input == 'scissors':
                print('Your input is paper')
                print('computer input is scissors')
                print('computer wins')
                user_points += 1
    
    elif user_input == 'scissors':
        if user_input == 'rock':
            if computer_input == 'rock':
                    print('Your input is scissors')
                    print('computer input is rock')
                    print('computer win!')
                    computer_points += 1
            elif computer_input == 'paper':
                    print('Your input is scissors')
                    print('computer input is paper')
                    print('you win')
                    user_points += 1
            elif computer_input == 'scissors':
                    print('Your input is scissors')
                    print('computer input is scissors')
                    print('its a tie!')

    elif user_input != 'rock' or user_input != 'paper' or user_input != 'scissors':
        print('Invalid input')