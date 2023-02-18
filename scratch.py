# # EXAMPLE FROM CLASS
def play_game():

    word = 'apple'
    wrong_guesses = ['b', 'd']
    right_guesses = ['a', 'p']
    game_board = ''

    for letter in word:
        if letter in right_guesses:
            game_board += letter + ' '
        else:
            game_board += '_ '
    print(game_board)


# DO NOT CHANGE CODE BELOW THIS LINE !!!
if __name__ == "__main__":
    play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
