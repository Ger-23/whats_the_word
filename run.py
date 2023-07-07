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
    Chooses random word from word list and returns a word from said list, in all caps.
    """
    random_word_index = random.randint(0, len(WORD_LIST) -1)
    return WORD_LIST[random_word_index].upper()

random_word = choose_word()
print("Random word:", random_word)


#def wtw():

#wtw()