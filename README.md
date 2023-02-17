# Hangman-game / word guessing game

The following code is an implementation of the game Hangman. The first two lines import the random module and a list of words called word_list from a separate file called hangman_words.py.

Next, the code randomly chooses a word from word_list using the random.choice() function and assigns it to a variable called chosen_word. The length of chosen_word is also calculated and stored in a variable called word_length.

The code then sets some initial variables for the game: end_of_game is set to False, lives is set to 6, and an empty list called display is created.

The Hangman logo is then printed to the console using the print() function, and a for loop is used to create a list of underscores that is the same length as the chosen word. The display list is then printed to the console, separated by spaces.

The code then enters a while loop that will continue until end_of_game is set to True. Each iteration of the loop asks the user to guess a letter using the input() function, and the letter is converted to lowercase using the lower() method. If the guessed letter is already in the display list, a message is printed to the console informing the user that the letter has already been guessed.

The loop then iterates over each character in the chosen_word, checking if the guessed letter matches the current character. If it does, the corresponding underscore in the display list is replaced with the correct letter.

If the guessed letter is not in the chosen_word, the player loses a life and a message is printed to the console. If the player has no lives left, the game ends and the word is revealed.

The display list is then printed to the console, with spaces separating the characters. If all the letters have been correctly guessed, the game ends and a message is printed to the console informing the user that they have won.

Finally, the Hangman ASCII art is printed to the console based on the current number of lives, and the number of remaining lives is printed to the console.
