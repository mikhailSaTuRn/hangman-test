import random
print("H A N G M A N")

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    input_letters = []
    tries = 8
    word = random.choice(words)
    letter_list = list(word)
    guessed = "-" * len(word)
    guessed_list = list(guessed)
    pos_chars = 'abcdefghijklmnopqrstuvwxyz'

    while tries > 0:
        print()
        print(''.join(guessed_list))
        # input letters
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should print a single letter")
            continue
        elif letter not in list(pos_chars):
            print("It is not an ASCII lowercase letter")
            continue
        # goal or missed
        if letter in input_letters:
            print('You already typed this letter')
            continue
        input_letters.append(letter)
        if letter not in letter_list:
            print('No such letter in the word')
            tries -= 1
        if tries == 0:
            print('You are hanged!')
            print()
            break
        # guessed letters or dashes
        i = 0
        while i < len(word):
            if letter == word[i]:
                guessed_list[i] = letter_list[i]
            i = i+1
        if guessed_list == letter_list:
            print()
            print(''.join(guessed_list))
            print("You guessed the word!")
            print('You survived!')
            print()
            break
    menu()

def menu():
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == 'play':
        print()
        hangman()
    elif mode == 'exit':
        pass
    else:
        menu()
        
menu()
