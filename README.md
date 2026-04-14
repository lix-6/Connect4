# Connect 4 – Two-Player Terminal Game
A classic Connect 4 (Four in a Row) game implemented in Python, designed for two players to play in the terminal.
This project was originally created as a first-year programming assignment.

# Description
Connect 4 is a two-player connection game in which players take turns dropping colored discs into a vertically suspended 6×7 grid.
The goal is to be the first to form a horizontal, vertical, or diagonal line of four discs.
This terminal-based version uses simple text graphics to display the board and handles user input with basic validation.

# Features
- Two-player local gameplay (X and O)
- Clear board display with column labels (A–G)
- Input validation (column full, out-of-range, non-numeric)
- Win detection in all four directions
- Draw detection when the board is full
- Option to quit at any time

# How to Play
1. Run the script: `python connect4.py`
2. Choose **1** to start a new game, or **2** to exit.
3. Players alternate turns. Player **X** goes first.
4. On your turn, enter a column number from **1 to 7** (where 1 = A, 7 = G).
5. Your disc will drop to the lowest available row in that column.
6. The game announces a winner or a draw when the board is full.
7. Enter `q` at any time during a game to quit.
