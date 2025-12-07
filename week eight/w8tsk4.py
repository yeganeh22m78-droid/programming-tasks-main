# File: time_lib.py
# Library for handling timestamps

from datetime import datetime
from typing import List

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: List[datetime]) -> None:
    """Read timestamps from file and append to PTimestamps list."""
    PTimestamps.clear()
    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # skip empty lines
                    try:
                        # Format: YYYY-MM-DD HH:MM
                        ts = datetime.strptime(line, "%Y-%m-%d %H:%M")
                        PTimestamps.append(ts)
                    except ValueError:
                        print(f"Skipping invalid timestamp: {line}")
    except FileNotFoundError:
        print(f"File '{PFilename}' not found.")

def calculateYears(PYear: int, PTimestamps: List[datetime]) -> int:
    return sum(1 for ts in PTimestamps if ts.year == PYear)

def calculateMonths(PMonth: str, PTimestamps: List[datetime]) -> int:
    if PMonth not in MONTHS:
        print("Invalid month name.")
        return 0
    month_index = MONTHS.index(PMonth) + 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)

def calculateWeekdays(PWeekday: str, PTimestamps: List[datetime]) -> int:
    if PWeekday not in WEEKDAYS:
        print("Invalid weekday name.")
        return 0
    return sum(1 for ts in PTimestamps if ts.strftime("%A") == PWeekday)
