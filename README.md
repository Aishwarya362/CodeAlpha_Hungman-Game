# Hangman

A classic word-guessing game written in Python. The computer picks a random word and you guess it one letter at a time. You can make up to **6 wrong guesses** before the game ends.

## How to Play

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/hangman.git
   cd hangman
   ```
2. Run the game (Python 3.7+ required, no external dependencies):
   ```bash
   python hangman.py
   ```
3. Enter a single letter when prompted.

## Rules

- A random word is chosen from a fixed list of 5 words.
- Type **one letter** per turn.
- Correct letters are revealed in the word.
- Each wrong guess costs one of your **6 lives**.
- Guess the full word before running out of lives to win!

## Example Run

```
Welcome to Hangman!
You have 6 incorrect guesses allowed. Good luck!

Word: _ _ _ _ _ _
Guessed letters: none
Wrong guesses left: 6
Guess a letter: e
Good guess! "e" is in the word.
```

## Project Structure

```
hangman/
├── hangman.py   # The game (single file)
└── README.md    # This file
```

## License

MIT — free to use and modify.
