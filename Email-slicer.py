from distutils import extension


def main():
    print('This is my email slicer')
    print('')

    email_input = input('Enter your email address: ')

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    main()