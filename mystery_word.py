import random

# should be able to delete lower case now that player_guess is capitalized when submitted
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def select_word(file):
    with open(file) as opened_file:
        words_list = opened_file.read().splitlines()
        game_word = random.choice(words_list).upper()
    print(game_word)
    return game_word


def play_game():

    game_word = select_word('words.txt')
    remaining_guesses = 8
    game_letters = [*game_word]
    fixed_game_letters = list(set(game_letters))
    # turn list into set then back into list to remove duplicate letters
    guessed_letters = []
    possible_letters = ALPHABET

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
    player_guess = input("Guess a letter! ").upper()

    # will have a while loop that contains if loop
    # while remaining_guesses != 0 && game_letters != []

    if player_guess not in possible_letters:
        refresh_game_board()
        print("Try again. Guess ONE letter.")
    elif player_guess in fixed_game_letters:
        fixed_game_letters.remove(player_guess)
        # print(fixed_game_letters)


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
