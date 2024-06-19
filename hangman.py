import random

def choose_word():
    # List of words for the game
    words = ["python", "hangman", "programming", "computer", "science", "algorithm", "openai", "language"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6  # Number of tries allowed

    while tries > 0:
        # Display current state of word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if display_word.replace(" ", "") == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            tries -= 1
            print("Wrong guess! You have", tries, "tries left.")

    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", word)

if __name__ == "__main__":
    print("Welcome to Hangman!")
    play_hangman()
