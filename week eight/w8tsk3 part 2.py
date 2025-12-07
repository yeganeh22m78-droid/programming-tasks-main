# File: A8_T3.py
# Menu-driven program for analysing number files

import number_lib

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1

def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            filename = input("Insert filename: ")
            values = number_lib.readValues(filename)
        elif choice == 2:
            print(f"Amount of values {len(values)}")
        elif choice == 3:
            result = number_lib.calculateSum(values)
            print(f"Sum of values {result}")
        elif choice == 4:
            result = number_lib.calculateAverage(values)
            print(f"Average of values {result}")
        else:
            print("Invalid choice. Please try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
