# Simple program that can perform basic math operations on two numbers.
# Includes a bonus game!
# by: William Moule-Fortin (moul0087)

import random
from time import sleep

def rock_paper_scissors():
    """Bonus minigame!"""
    possibilities = ['Rock', 'Paper', 'Scissors']
    while True:
        computer_selection = random.choice(possibilities)
        while True:
            user_selection = input("1. Rock\n2. Paper\n3. Scissors\nMake your selection: ")
            if user_selection not in ['1', '2', '3']:
                print("Invalid input. Please enter a number from 1 to 3.")
                continue
            else:
                user_selection = possibilities[int(user_selection)-1]
                break

        print(f"\nYour selection: {user_selection}")
        sleep(1)
        for i in range(3):
            print(possibilities[i]+'!')
            sleep(1)
        print("Shoot!")
        sleep(1)
        print(f"Computer selection: {computer_selection}")

        if computer_selection == user_selection:
            print("Same result. Draw.")
        elif (computer_selection, user_selection) in {('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors', 'Rock')}:
            print("You won!")
        else:
            print("You lose. Better luck next time!")
        while True:
            replay = input("Play again? (y/n): ")
            if replay.lower() not in ['y', 'n']:
                print("Invalid input. Please type y or n.")
            else:
                break
        if replay.lower() == 'y':
            continue
        else:
            break


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def user_interact():
    """User interaction function for use in main loop."""
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            return x, y

def main():
    """Main program loop, containing user interface and option selection."""
    while True:
        print("2 NUMBER CALCULATOR"
              "\n---- Menu ----"
              "\n1. Multiply"
              "\n2. Divide"
              "\n3. Add"
              "\n4. Subtract"
              "\n5. Bonus!"
              "\nQ. Exit")
        user_input = input("Enter your selection: ")
        print()
        if user_input == "1":
            x, y = user_interact()
            print(f"{multiply(x, y)}\n")
        elif user_input == "2":
            x, y = user_interact()
            if y == 0:
                print("Error. Cannot divide by zero.\n")
            else:
                print(f"{divide(x, y)}\n")
        elif user_input == "3":
            x, y = user_interact()
            print(f"{add(x, y)}\n")
        elif user_input == "4":
            x, y = user_interact()
            print(f"{subtract(x, y)}\n")
        elif user_input == "5":
            rock_paper_scissors()
        elif user_input.lower() == "q":
            break
        else:
            print("Error. Please select a valid option.")
main()