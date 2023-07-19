import os
import random

def clear_screen():
    # Function to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = [word.strip() for word in content.split(', ')]
    return words

def play_memory_game(words, level):
    clear_screen()
    print(f"Level {level}:")
    print("***************************")
    print(f"Remember the word: {words[level-1]}")
    print("***************************")
    user_input = input("Enter the word(s) separated by comma and space: ")
    user_words = [word.strip() for word in user_input.split(',')]
    expected_words = words[:level]
    
    if len(user_words) != level or not all(word.lower() == expected_words[i].lower() for i, word in enumerate(user_words)):
        print("Game Over! You made a mistake.")
        print(f"The correct answer should have been: {', '.join(expected_words)}")
        return False
    
    print("Congratulations! You passed the level.")
    return True


def main():
    file_path = "words.txt"  # Path to the external txt file
    words = load_words(file_path)
    random.shuffle(words)

    print(""" __ __   ___   __ __    __    ___   __   __    __    __    __ __   ___  
|  V  | | __| |  V  |  /__\  | _ \  \ `v' /   / _]  /  \  |  V  | | __| 
| \_/ | | _|  | \_/ | | \/ | | v /   `. .'   | [/\ | /\ | | \_/ | | _|  
|_| |_| |___| |_| |_|  \__/  |_|_\    !_!     \__/ |_||_| |_| |_| |___| 

""")
    print("****************************")
    print("Enter each word separated by comma and space (e.g., apple, orange, banana).")

    max_level = 0
    for level in range(1, len(words) + 1):
        if play_memory_game(words, level):
            print("****************************")
            print("Level completed! Proceeding to the next level.")
            max_level = level
        else:
            print("****************************")
            print("Game Over! Try again.")
            break
    
    print(f"Max level reached: {max_level}")

if __name__ == '__main__':
    main()

