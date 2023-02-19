import random

# list of capitalized letters; will be used as possible_letters
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z']

# # SEPARATE WORDS INTO LISTS BASED ON LENGTH
# def create_words_lists(file):
#     easy_words = []
#     medium_words = []
#     hard_words = []
#     insane_words = []
#     with open(file) as opened_file:
#         words_list = opened_file.read().splitlines()
#         for word in words_list:
#             if len(word) > 2 and len(word) < 5:
#                 easy_words.append(word)
#             elif len(word) > 4 and len(word) < 7:
#                 medium_words.append(word)
#             elif len(word) > 6 and len(word) < 9:
#                 hard_words.append(word)
#             elif len(word) > 8:
#                 insane_words.append(word)
#     return easy_words, medium_words, hard_words, insane_words


def select_word(file):
    with open(file) as opened_file:
        words_list = opened_file.read().splitlines()
        game_word = random.choice(words_list).upper()
    # print(game_word)
    return game_word


# MAIN FUNCTION
def play_game():

    game_word = select_word('words.txt')
    remaining_guesses = 8
    game_letters = [*game_word]
    fixed_game_letters = list(set(game_letters))
    chosen_game_letters = []
    guessed_letters = []
    possible_letters = ALPHABET

    # tried to figure out how to have this function outside of play_game and call it
    def update_word_display():
        blank_word = ''
        for letter in game_word:
            if letter in chosen_game_letters:
                blank_word += letter + ' '
            else:
                blank_word += '_ '
        print(blank_word)
        return blank_word

    # made this to simplify code
    def update_game_board():
        print(' \n ')
        print("Letters Guessed: " + str(guessed_letters))
        print("Chances Left: " + str(remaining_guesses))

    # OPENING GAME BOARD
    update_game_board()
    update_word_display()
    print("Welcome to Mystery Word!")
    print("Ready to play?")

    while remaining_guesses > 0:
        player_guess = input("Guess a letter! ").upper()
        if player_guess not in possible_letters:
            print("Your guess must be a single letter. Try again!")

        elif player_guess in guessed_letters:
            print("You've already guessed that letter. Try again!")

        elif player_guess in fixed_game_letters:
            fixed_game_letters.remove(player_guess)
            guessed_letters.append(player_guess)
            chosen_game_letters.append(player_guess)
            update_game_board()
            update_word_display()

            if len(fixed_game_letters) == 0:
                print("YOU WIN!")
                break
            else:
                print("Great job! You got one!")

        else:
            guessed_letters.append(player_guess)
            remaining_guesses -= 1
            update_game_board()
            update_word_display()
            print("Oops! Try again!")

    else:
        update_game_board()
        print("The mystery word was: " + game_word)
        print("YOU LOSE!")

    play_again = input("Would you like to play again Y/N? ").upper()
    if play_again == 'Y':
        play_game()


# DO NOT CHANGE CODE BELOW THIS LINE !!!
if __name__ == "__main__":
    play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
