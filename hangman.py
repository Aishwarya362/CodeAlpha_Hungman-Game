import random


def play_hangman():
    # 1. A small list of 5 predefined words
    words = ["python", "garden", "planet", "monkey", "rocket"]

    # 2. Pick a random word
    word = random.choice(words)
    guessed_letters = []      # letters the player has guessed
    wrong_guesses = 0         # count of incorrect guesses
    max_wrong = 6             # limit of incorrect guesses

    print("Welcome to Hangman!")
    print(f"You have {max_wrong} incorrect guesses allowed. Good luck!\n")

    # 3. Keep playing while guesses remain and word isn't fully revealed
    while wrong_guesses < max_wrong:
        # Build the display: show letter if guessed, else "_"
        display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'none'}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You win! The word was \"{word}\".")
            break

        # 4. Get a valid guess from the player
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # 5. Record the guess and check if it's right
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good guess! \"{guess}\" is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Nope! \"{guess}\" is not in the word.\n")
    else:
        # 6. Ran out of guesses (while loop ended without break)
        print(f"💀 Game over! The word was \"{word}\". Better luck next time!")


# Start the game
if __name__ == "__main__":
    play_hangman()
