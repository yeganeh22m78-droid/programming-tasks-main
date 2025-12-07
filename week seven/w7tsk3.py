WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    """Reads the CSV file and fills PRows with non-empty data rows (skipping header)."""
    print(f'Reading file "{PFilename}".')
    PRows.clear()
    try:
        with open(PFilename, "r") as f:
            header_skipped = False
            for line in f:
                if not header_skipped:
                    header_skipped = True
                    continue  # skip header
                line = line.strip()
                if line:
                    PRows.append(line)
    except FileNotFoundError:
        print(f'Error: The file "{PFilename}" does not exist.')

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    """Analyses timestamps per weekday and fills PResults list."""
    print("Analysing timestamps.")
    PResults.clear()
    WeekdayTimestampAmount = [0] * len(WEEKDAYS)
    
    for row in PRows:
        for j, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[j] += 1
                break

    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")

def displayResults(PResults: list[str]) -> None:
    """Displays the analysis results."""
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")

def main() -> None:
    print("Program starting.")
    
    Rows: list[str] = []
    Results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)
    Rows.clear()
    Results.clear()
    print("Program ending.")

main()
