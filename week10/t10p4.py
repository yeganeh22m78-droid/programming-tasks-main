import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or (not PAsc and PValues[j] < PValues[j + 1]):
                # Swap
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
    return None

def readValues(filename: str) -> list[int]:
    values = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    values.append(int(line))
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error! Cannot convert line to integer: {ve}")
        sys.exit(1)
    return values

def main() -> None:
    print("Program starting.")

    # Get filename from CLI or prompt
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values = readValues(filename)

    # Display raw values
    print(f"Raw '{filename}' -> {', '.join(str(v) for v in value
