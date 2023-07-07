import random

WORD_LIST = [
    "Homer",
    "Apu",
    "Smithers",
    "Flanders",
    "Barney"
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

    print(' '.join(dashed_word))
    
test_word = "HOUSE"
guessed_letters = ["O", "E"]
print(test_word, guessed_letters)
dashed_word_rep(test_word, guessed_letters)

#def wtw():

#wtw()