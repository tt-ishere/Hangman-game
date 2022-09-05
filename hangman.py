import random
from hangman_words import word_list

#randomly choosing a word from the imported word_list 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#variables
end_of_game = False
lives = 6
display = []

#Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the chosen word is {chosen_word}.')

#Creating blanks in display list
for _ in range(word_length):
    display.append("_")
print(*display, sep = " ")
print("\n") #creating a line break to make it easy on the eyes

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("\n")

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have guessed {guess} already\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f'"{guess}" is not in the word \nYou have lost a life\n')
        if lives == 0:
            end_of_game = True
            print(f"Hangman word is {chosen_word}")
            print("You lose.")
            

    #Join all the elements in the list and turn it into a String.
    print(*display, sep = " ")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py.
    from hangman_art import stages
    
    print(stages[lives])
    print(f"Lives: {lives}\n")