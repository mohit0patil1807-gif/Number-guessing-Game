# Number Guessing Game

A command-line number guessing game built with Python. The player attempts to guess a randomly generated number between 1 and 100 within a limited number of attempts based on the selected difficulty level.

## Overview

The Number Guessing Game is a classic terminal-based game. When the game starts, a random number between 1 and 100 is chosen. The player selects a difficulty level (Easy or Hard) and receives hints after each guess indicating whether the guess was too high or too low until they find the answer or run out of attempts.

## Features

- Random Number Generation: A secret number between 1 and 100 is selected for each game.
- Two Difficulty Levels:
  - Easy Mode: 10 attempts to find the number.
  - Hard Mode: 5 attempts to find the number.
- Dynamic Feedback: After each attempt, the game provides guidance ("too high" or "too low").
- ASCII Banner: Displays an ASCII art title banner at the start of the session.
- Turn Tracking: Displays remaining attempts after each guess.

## How the Game Works

1. The game initializes and presents the ASCII art header.
2. The computer selects a random number between 1 and 100.
3. The user selects a difficulty:
   - Type 'easy' for 10 attempts.
   - Type 'hard' for 5 attempts.
4. The user enters a numeric guess.
5. If the guess is correct, the user wins and the game concludes.
6. If the guess is incorrect, the program informs the user whether the guess was "too high" or "too low", decrements the turn counter by one, and prompts for the next guess.
7. If turns reach zero, the game ends and reveals the secret number.

## Project Structure

```
Number-guessing-game/
|-- art.py          # Contains the ASCII banner art
|-- main.py         # Main game logic and loop
|-- .gitignore      # Git ignore configuration
`-- README.md       # Project documentation
```

## Prerequisites

- Python 3.6 or higher installed on your system.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mohit0patil1807-gif/Number-guessing-Game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Number-guessing-Game
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Example Gameplay

```text
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 

Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 turns left
Make a guess: 50
too high
You have 9 turns left
Make a guess: 25
too low
You have 8 turns left
Make a guess: 37
You got it! The answer was 37
```

## Author

- mohit0patil1807-gif
- GitHub: https://github.com/mohit0patil1807-gif
