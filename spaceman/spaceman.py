import random

def load_word():
 
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    progress = ''
    for i in secret_word:
        if i in letters_guessed:
            progress += i
        else:
            progress += '_'
    return progress

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    return False


def spaceman(secret_word):
    fails = 7
    letters_guessed = ''
    guesses = []
    won = False

    print("Welcome to Spaceman!")
    print(f"The secret word contains: {len(secret_word)} letters")
    print("You have 7 incorrect guesses, please enter one letter per round")
    # print(secret_word) # FOR TESTING
   

    while fails < 8 and not won:
        print('---------------------------------------------------------------')
        guess = str(input("Enter a letter: "))
        if guess not in guesses:
            if is_guess_in_word(guess, secret_word):
                letters_guessed += guess
                print()
                print('yep! nice!')
            else:
                fails -= 1
                print()
                print('nope!')
                print(f"You have {fails} incorrect guesses left.")

            guesses+=guess

        else:
            print()
            print("you already guessed that silly!")

        print()
        print(get_guessed_word(secret_word, letters_guessed))
        print()

        if is_word_guessed(secret_word, letters_guessed): # HELP
            won = True

    if(won):
        print("you won! congrats!")
    else:
        print("you lost. next time:/")



def test():
    # print(is_word_guessed('cool', ['c', 'o', 'o', 'l']))
    # print(get_guessed_word('cool', ['c', 'e', 'l']))
    print(is_guess_in_word('e', 'cool'))

# RUN GAME --------------------------------------------- #
secret_word = load_word()
spaceman(secret_word)

# test()