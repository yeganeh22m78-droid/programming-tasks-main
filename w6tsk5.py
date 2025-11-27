SEPARATOR = ";"  # For CSV formatting

def readValues(filename):
    """Read integer numbers from a text file and return as a string with separator."""
    values_str = ""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                number = int(line.strip())  # Convert line to integer
                values_str += str(number)
                if i < len(lines) - 1:
                    values_str += SEPARATOR
        return values_str
    except FileNotFoundError:
        print(f'Error: The file "{filename}" does not exist.')
        return ""

def analyseNumbers(values_str):
    """Analyse the numbers provided as a separator-separated string."""
    if not values_str:
        return "0;0;0;0.00"
    
    numbers = [int(v) for v in values_str.split(SEPARATOR)]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    return f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"

def displayResults(filename, analysis_result):
    """Print results in the required CSV format."""
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(f"Count{SEPARATOR}Sum{SEPARATOR}Greatest{SEPARATOR}Average")
    print(analysis_result)
    print("\n#### Number analysis - END ####")

# Main program
print("Program starting.")
filename = input("Insert filename: ")
values_str = readValues(filename)
analysis_result = analyseNumbers(values_str)
displayResults(filename, analysis_result)
print("Program ending.")
