import random

# open text file, read it, turn it into a list of strings
WORDS_LIST = open('words.txt').read().splitlines()
# print(WORDS_LIST)

# game_word = random.choice(WORDS_LIST).upper()
# print(game_word)

# game_letters = [*game_word]
# print(game_letters)

# NOT WORKING !!!


# def choose_random_word():
#     word_list = ['apple', 'brain', 'container', 'donkey', 'eating']
#     print(word_list)
#     game_word = (random.choice(word_list))
#     print(game_word)


# GET A LIST OF LETTERS FROM THE WORD
# 'apple' --> ['a', 'e', 'l', 'p']


def play_game():
    # choose_random_word()
    word = 'apple'
    print(len(word)*'_ ')
    # will need other lists:
    # correct_letters = ['a', 'e', 'l', 'p'] --> letters are removed then added to guessed_letters
    # guessed_letters = [] --> letters are added when guessed
    wrong_guesses = ['b', 'd']
    right_guesses = ['a', 'p']

    game_board = ''
    for letter in word:
        if letter in right_guesses:
            game_board += letter + ' '
        # if letter in correct_guesses:
            #
        else:
            game_board += '_ '
    print(game_board)


# DO NOT CHANGE CODE BELOW THIS LINE !!!
if __name__ == "__main__":
    play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
