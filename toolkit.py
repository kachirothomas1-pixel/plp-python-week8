# toolkit.py - Personal Mini-Toolkit Final Project
# Author: Kachiro Thomas
# Description: A menu-driven Python application offering three tools (Number Guessing Game,
# To-Do List Manager, and Temperature Converter) utilizing loops, lists, and conditionals.

import random

def number_guessing_game():
    """A number guessing game using a loop and conditionals."""
    secret_number = random.randint(1, 10)
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number {secret_number}.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def todo_list_manager(tasks):
    """A to-do list manager using a list that changes while the program runs."""
    print("\n--- To-Do List Manager ---")
    while True:
        print(f"\nCurrent Tasks: {tasks}")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            new_task = input("Enter the task to add: ")
            tasks.append(new_task)
            print(f"Added '{new_task}' successfully!")
        elif choice == '2':
            rem_task = input("Enter the task to remove: ")
            if rem_task in tasks:
                tasks.remove(rem_task)
                print(f"Removed '{rem_task}' successfully!")
            else:
                print("Task not found in the list.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def temperature_converter():
    """A temperature converter using conditionals and f-strings."""
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose conversion type (1 or 2): ")
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is equal to {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F is equal to {c:.2f}°C")
    else:
        print("Invalid conversion choice.")

def main():
    """Main function running the menu loop with input validation."""
    my_tasks = ["Buy groceries", "Study Python"]
    
    print("👋 Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n==============================")
        print("      PERSONAL MINI-TOOLKIT    ")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. To-Do List Manager")
        print("3. Temperature Converter")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            todo_list_manager(my_tasks)
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("\n👋 Thank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
