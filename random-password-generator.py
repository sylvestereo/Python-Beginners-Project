import string
import random

characters = list(string.ascii_letters + string.digits + "!£$%^&*()_+:@~?><,./#;")
def generate_password():
    password_length = int(input("How long do you want your password? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)


    password = "".join(password)

    print(password)

option = input("Do you want to generate a pasword? (Y/N): ")

if option == 'Y':
    generate_password()
elif option == 'N':
    print('Program terminated')
    quit()
else:
    print('Please enter a valid option')
    quit()