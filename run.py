import random

WORD_LIST = [
    "HOMER",
    "APU",
    "SMITHERS",
    "FLANDERS",
    "BARNEY",
    "MARGE",
    "MAGGIE",
    "LISA",
    "BART",
    "MOE",
    "MRBURNS",
    "MAUDE",
    "PATTY",
    "SELMA",
    "GRANDPA",
    "LENNY",
    "CARL",
    "DUFFMAN"
]

MAX_LIVES = 5

def choose_word():
    """
    Choose random word from word list and returns a word from said list, in all caps.
    """
    random_word_index = random.randint(0, len(WORD_LIST) -1)
    return WORD_LIST[random_word_index].upper()


def dashed_word_rep(word, guessed_letters):
    """
    Print dashed representation of chosen word.
    """
    dashed_word = []
    for letter in word:
        if letter in guessed_letters:
            dashed_word.append(letter)
        else:
            dashed_word.append('_')
    
    return(' '.join(dashed_word))



def wtw():
    """
    implement game logic. Prompt player to enter guess, check if correct, incorrect or repeat guess, and update guessed letters and lives left.
    """
    
    print("Welcome to What's The Word!")
    print("The object of the game is to guess the letters to reveal the hidden word.\nYou have a total of 5 lives.\nGood luck!")
    print("Theme is characters from The Simpsons")

while True:

    wtw()
    current_word = choose_word()
    guessed_letters = []
    lives_left = MAX_LIVES

    
    print(dashed_word_rep(current_word, guessed_letters))
    
    while True:
        guess = input("Guess a letter:\n").upper()

        if guess in guessed_letters:
            print("You've already guessed that one!")
            continue

        guessed_letters.append(guess)

        if guess in current_word:
            print("Correct guess!")
        else:
            lives_left -= 1
            print("Incorrect guess!")
            print("Lives left: ", lives_left)

        dashed_word = dashed_word_rep(current_word, guessed_letters)
        print(dashed_word)

        if lives_left == 0:
            print("No lives left! Better luck next time!")
            break

        if '_' not in dashed_word_rep(current_word, guessed_letters):
            print("Congratulations! You've guessed the word! Well done!")
            break

    play_again = input("Would you like to have another go? (y/n?): \n")
    if play_again.lower() != 'y':
        break

