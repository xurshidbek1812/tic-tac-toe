# Tic-Tac-Toe with AI

A command-line Tic-Tac-Toe game written in Python. Play against a computer opponent that uses the **Minimax algorithm** to evaluate possible moves and make optimal decisions.

## Features

- Play as either X or O.
- Computer opponent powered by Minimax.
- AI evaluates possible future game states before choosing a move.
- Automatically detects wins, losses, and draws.
- Prevents players from making invalid moves.
- 3×3 game board displayed in the terminal.

## Requirements

- Python 3.10 or newer.

No external libraries are required.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

## Run the Game

Execute:

```bash
python3 tic-tac-toe.py
```

## How to Play

1. Run the program.
2. Choose your side (`X` or `O`).
3. Enter a number between 1 and 9 to select a position.
4. The computer automatically makes its move.
5. Continue until someone wins or the game ends in a draw.

### Board Position Reference

```text
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

## AI Algorithm: Minimax

The computer uses the Minimax algorithm, a recursive decision-making algorithm commonly used in two-player, zero-sum games.

It explores possible future moves and evaluates the resulting game states.

### Evaluation Values

| Value | Meaning |
|---|---|
| `1` | X wins |
| `-1` | O wins |
| `0` | Draw |
| `2` | Game is not finished |

### How It Works

- X tries to maximize the evaluation score.
- O tries to minimize the evaluation score.
- The algorithm recursively explores available moves.
- The computer selects a move based on the best possible outcome.

Because Tic-Tac-Toe is a solved game, optimal play guarantees that the computer will never lose.

## Project Structure

```text
tic-tac-toe/
│
├── tic-tac-toe.py
└── README.md
```

## Technologies

- Python
- Object-Oriented Programming (OOP)
- Recursion
- Minimax Algorithm
- Two-dimensional Lists

## License

This project is open-source and available for educational and personal use.
