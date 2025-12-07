import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    PMerge.clear()
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    # Append remaining elements
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)
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
    print(f"Raw '{filename}' -> {', '.join(str(v) for v in values)}")

    # Sort ascending
    mergeSort(values, PAsc=True)
    print(f"Ascending '{filename}' -> {', '.join(str(v) for v in values)}")

    # Sort descending
    mergeSort(values, PAsc=False)
