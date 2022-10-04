def main():
    word_dictionary = {
        'hi': 'A way of greeting',
        'eyes': 'A seeing organ',
        'earth': 'a planet in space',
    }

    while True:
        word = input('Enter your word: ')
        if word == '':
            break
        if word in word_dictionary:
            print(word, ':', word_dictionary[word])

main()
