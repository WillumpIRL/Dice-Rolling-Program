# Dice Roller 1984

## Description
Dice Roller 1984 is a simple Python program that allows users to roll dice in various configurations, including support for standard rolls and exploding dice mechanics. It provides statistics on the rolls, such as total sum, average, minimum, and maximum values.

## Features
- Roll any number of dice with a specified number of sides (e.g., `4d6` for rolling four six-sided dice).
- Support for exploding dice using the `!` symbol (e.g., `4d6!` will reroll and add dice that land on their max value).
- Displays individual rolls, total sum, average, minimum, and maximum values.
- Simple and intuitive command-line interface.
- Help menu for guidance on usage.

## Installation
No installation is required. Ensure you have Python installed (version 3.x recommended) and download or copy the script.

## Usage
1. Run the script in a terminal or command prompt:
   ```sh
   python dice_roller.py
   ```
2. Enter a roll command in the format:
   ```
   (quantity)d(sides)
   ```
   Example:
   ```
   10d12
   ```
   This rolls ten twelve-sided dice.
3. To enable exploding dice, add `!` at the end:
   ```
   4d6!
   ```
   This will reroll any dice that land on their maximum value and add them to the total.
4. For help, enter:
   ```
   h
   ```
5. To exit, enter:
   ```
   x
   ```

## Example Output
```
Enter Your Roll (or "h" for help, "x" to close): 3d6
Now Rolling 3d6

Roll 1 of 3. Rolled a 4!
Roll 2 of 3. Rolled a 2!
Roll 3 of 3. Rolled a 5!
============================================================
||                        STATS                           ||
============================================================
Rolls:  [4, 2, 5]
Total:  11
Average:  3.67
Minimum:  2 (1 occurrence)
Maximum:  5 (1 occurrence)
```

## Notes
- The program enforces valid input formats. If an invalid input is entered, an error message will appear.
- Dice rolls must have at least one die and a minimum of two sides.

## License
This program is provided as-is with no warranty. Feel free to modify and distribute it as needed.

## Author
Created by [William James].

