import random

def roll_dice():

    
    roll = input('Roll the dice? (Y/N): ')

    while roll.lower() == 'Y'.lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (Y/N): ")

roll_dice()