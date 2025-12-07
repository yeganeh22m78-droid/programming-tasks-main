import sys
from functools import reduce
import operator

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error! Cannot convert line to integer: {ve}")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    return reduce(operator.mul, PValues, 1)

def main() -> None:
    Values: list[int] = []

    print("Program starting.")

    # 1. Ask filename
    filename = input("Insert filename: ")

    # 2. Read values
    readValues(filename, Values)

    # 3. Calculate sum
    total = sumOfValues(Values)
    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")

    # 4. Calculate product
    prod = productOfValues(Values)
    print("# --- Product of numbers --- #")
    print(prod)
    print("# --- Product of numbers --- #")

    # 5. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
