DELIMITER = ";"

# Define a simple class to store timestamp data
class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

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
                    continue  # skip header
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

def displayTimestamps(timestamps: list) -> None:
    """Print each timestamp with consumption, price, and total cost."""
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
              f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €")

def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    displayTimestamps(timestamps)

    timestamps.clear()
    print("Program ending.")

main()
