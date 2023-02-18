import random

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def select_word(file):
    with open(file) as opened_file:
        words_list = opened_file.read().splitlines()
        # open words.txt, read it, split it into a list of strings
        game_word = random.choice(words_list).upper()
        # randomly select a word and capitalize it
    # print(game_word)
    return game_word


def play_game():

    game_word = select_word('words.txt')
    remaining_guesses = 8
    game_letters = [*game_word]
    # print(game_letters)
    # turn into list of letters; letters are removed then added to guessed_letters
    guessed_letters = []
    # make list for guessed letters; letters are added when guessed
    possible_letters = ALPHABET
    # list of the alphabet; if guess is not in this list, print a message to guess again with a letter

    # GAME BOARD
    # make some kind of border??
    display_guessed_letters = "Letters Guessed: " + str(guessed_letters)
    display_remaining_guesses = "Chances Left: " + str(remaining_guesses)
    blank_word = len(game_word)*'_ '
    # print("Greeting/Response")
    # player_guess = input("Guess a letter! ")

    def refresh_game_board():
        print(display_guessed_letters)
        print(display_remaining_guesses)
        print(blank_word)

    refresh_game_board()
    print("Ready to play?")
    input("Guess a letter! ")

    if input not in possible_letters:
        refresh_game_board()
        print("Try again. Guess ONE letter.")
        input("Guess a letter! ")

# # # EXAMPLE FROM CLASS
# def play_game():
#     word = 'apple'
#     wrong_guesses = ['b', 'd']
#     right_guesses = ['a', 'p']

#     game_board = ''
#     for letter in word:
#         if letter in right_guesses:
#             game_board += letter + ' '
#         else:
#             game_board += '_ '
#     print(game_board)


# DO NOT CHANGE CODE BELOW THIS LINE !!!
if __name__ == "__main__":
    play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
