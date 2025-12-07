import sys

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

    # 1. Ask filename
    filename = input("Insert filename: ")

    # 2. Read values
    values = readValues(filename)

    # 3. Display raw values
    print(f"Raw '{filename}' -> {', '.join(str(v) for v in values)}")

    # 4. Display ascending
    asc_values = sorted(values)
    print(f"Ascending '{filename}' -> {', '.join(str(v) for v in asc_values)}")

    # 5. Display descending
    desc_values = sorted(values, reverse=True)
    print(f"Descending '{filename}' -> {', '.join(str(v) for v in desc_values)}")

    print("Program ending.")

if __name__ == "__main__":
    main()
