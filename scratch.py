import random


WORDS_LIST = open('words.txt').read().splitlines()
# print(WORDS_LIST)

# game_word = random.choice(WORDS_LIST).upper()
# print(game_word)

# game_letters = [*game_word]
# print(game_letters)


def play_game():
    # choose_random_word()
    game_word = random.choice(WORDS_LIST).upper()
    print(game_word)
    game_letters = [*game_word]
    print(len(game_word)*'_ ')
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
# if __name__ == "__main__":
# play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
