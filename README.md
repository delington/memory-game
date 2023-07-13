# Memory Game

```
 __ __   ___   __ __    __    ___   __   __    __    __    __ __   ___  
|  V  | | __| |  V  |  /__\  | _ \  \ `v' /   / _]  /  \  |  V  | | __| 
| \_/ | | _|  | \_/ | | \/ | | v /   `. .'   | [/\ | /\ | | \_/ | | _|  
|_| |_| |___| |_| |_|  \__/  |_|_\    !_!     \__/ |_||_| |_| |_| |___| 
```


This is a simple memory game implemented in Python. The game tests your memory skills by challenging you to remember and recall words in a given order. Each level increases the number of words to remember, providing an escalating difficulty.

## Features

- Multiple levels with increasing difficulty.
- Random selection of words from an external file.
- Case-insensitive word comparison.
- Clear instructions for user input format.
- Display of correct answer when the user makes a mistake.
- Tracking of the maximum level reached by the user.

## Instructions

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine or download the ZIP file.
3. Place a text file named `words.txt` in the same directory as the Python script.
4. Add your desired words to the `words.txt` file, separating them by a comma and space (e.g., `Apple, Orange, Banana`).
5. Open a terminal or command prompt and navigate to the directory where the script is located.
6. Run the game by executing the following command:

```bash
python memory_game.py
```

## Example run
```
****************************
Enter each word separated by comma and space (e.g., apple, orange, banana).
Level 1:
***************************
Remember the word: Guitar
***************************
Enter the word(s) separated by comma and space: guitar
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 2:
***************************
Remember the word: Grapefruit
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 3:
***************************
Remember the word: Butterfly
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit, butterfly
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 4:
***************************
Remember the word: Cat
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit, butterfly, cat
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 5:
***************************
Remember the word: Bird
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit, butterfly, cat, bird
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 6:
***************************
Remember the word: Sunflower
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit, butterfly, cat, bird, sunflower
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 7:
***************************
Remember the word: Sofa
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit, butterfly, cat, bird, sunflower, sofa
Congratulations! You passed the level.
****************************
Level completed! Proceeding to the next level.
Level 8:
***************************
Remember the word: Ocean
***************************
Enter the word(s) separated by comma and space: guitar, grapefruit
Game Over! You made a mistake.
The correct answer should have been: Guitar, Grapefruit, Butterfly, Cat, Bird, Sunflower, Sofa, Ocean
****************************
Game Over! Try again.
Max level reached: 7
```