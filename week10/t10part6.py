import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")

    # Collect factorial number from CLI argument or prompt
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print("Error! Argument must be an integer.")
            sys.exit(1)
    else:
        try:
            num = int(input("Insert factorial: "))
        except ValueError:
            print("Error! Input must be an integer.")
            sys.exit(1)

    # Calculate factorial
    result = recursiveFactorial(num)

    # Display result
    print(f"Factorial {num}!")
    print(f"{num} = {result}")

    print("Program ending.")

if __name__ == "__main__":
    main()
