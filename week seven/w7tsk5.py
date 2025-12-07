DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

# Class to store timestamp data
class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

# Class to store daily usage summary
class DAY_USAGE:
    def __init__(self):
        self.usage = 0.0
        self.cost = 0.0

def readFile(filename: str, timestamps: list) -> None:
    """Read CSV file into a list of TIMESTAMP objects."""
    print(f'Reading file "{filename}".')
    timestamps.clear()
    try:
        with open(filename, "r") as f:
            header_skipped = False
            for line in f:
                if not header_skipped:
                    header_skipped = True
                    continue
                line = line.strip()
                if line:
                    columns = line.split(DELIMITER)
                    ts = TIMESTAMP()
                    ts.weekday = columns[0]
                    ts.hour = columns[1]
                    ts.consumption = float(columns[2])
                    ts.price = float(columns[3])
                    timestamps.append(ts)
    except FileNotFoundError:
        print(f'Error: The file "{filename}" does not exist.')

def analyseConsumption(timestamps: list, day_usages: list) -> None:
    """Analyse daily usage and cost."""
    print("Analysing timestamps.")
    day_usages.clear()
    # Initialize helper list
    helper = [DAY_USAGE() for _ in WEEKDAYS]

    for ts in timestamps:
        for i, day in enumerate(WEEKDAYS):
            if ts.weekday == day:
                helper[i].usage += ts.consumption
                helper[i].cost += ts.consumption * ts.price
                break

    # Prepare results as strings
    for i, day in enumerate(WEEKDAYS):
        day_usages.append(f" - {day} usage {helper[i].usage:.2f} kWh, cost {helper[i].cost:.2f} €")

def displayResults(day_usages: list) -> None:
    """Display daily electricity usage summary."""
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for line in day_usages:
        print(line)
    print("### Electricity consumption summary ###")

def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    day_usages: list[str] = []

    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    analyseConsumption(timestamps, day_usages)
    displayResults(day_usages)

    timestamps.clear()
    day_usages.clear()
    print("Program ending.")

main()
