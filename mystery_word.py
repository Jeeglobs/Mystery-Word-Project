import random

# should be able to delete lower case now that player_guess is capitalized when submitted
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z']


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
    chosen_game_letters = []
    guessed_letters = []
    possible_letters = ALPHABET

    def update_word_display():
        blank_word = ''
        for letter in game_word:
            if letter in chosen_game_letters:
                blank_word += letter + ' '
            else:
                blank_word += '_ '
        print(blank_word)
        return blank_word

    # OPENING GAME BOARD
    print("Letters Guessed: " + str(guessed_letters))
    print("Chances Left: " + str(remaining_guesses))
    update_word_display()
    print("Ready to play?")

    # # PRINT LISTS
    # print(remaining_guesses)
    # print(guessed_letters)
    # print(fixed_game_letters)
    # print(chosen_game_letters)

    # while remaining_guesses > 0:
    for letter in game_word:
        player_guess = input("Guess a letter! ").upper()
        if player_guess not in possible_letters:
            print("Your guess must be a single letter. Try again!")

        elif player_guess in guessed_letters:
            print("You've already guessed that letter. Try again!")

        elif player_guess in fixed_game_letters:
            fixed_game_letters.remove(player_guess)
            guessed_letters.append(player_guess)
            chosen_game_letters.append(player_guess)
            print(' \n ')
            print("Letters Guessed: " + str(guessed_letters))
            print("Chances Left: " + str(remaining_guesses))
            update_word_display()
            print("Great job! You got one!")

        else:
            guessed_letters.append(player_guess)
            remaining_guesses -= 1
            print(' \n ')
            print("Letters Guessed: " + str(guessed_letters))
            print("Chances Left: " + str(remaining_guesses))
            update_word_display()
            print("Oops! Try again!")


# DO NOT CHANGE CODE BELOW THIS LINE !!!
if __name__ == "__main__":
    play_game()
# DO NOT CHANGE CODE ABOVE THIS LINE !!!
