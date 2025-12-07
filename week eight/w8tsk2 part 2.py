# File: A8_T2.py
# Menu-driven calculator program

import calculator_lib

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1

def askValue(PPrompt: str) -> float:
    while True:
        try:
            return float(input(PPrompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = calculator_lib.add(a, b)
            print(f"{a} + {b} = {result}")
        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = calculator_lib.subtract(a, b)
            print(f"{a} - {b} = {result}")
        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            result = calculator_lib.multiply(a, b)
            print(f"{a} * {b} = {result}")
        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            try:
                result = calculator_lib.divide(a, b)
                print(f"{a} / {b} = {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
