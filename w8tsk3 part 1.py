Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # File: number_lib.py
... # Library for analysing number files
... 
... from typing import List
... 
... def readValues(PFilename: str) -> List[float]:
...     values: List[float] = []
...     try:
...         with open(PFilename, "r") as file:
...             for line in file:
...                 line = line.strip()
...                 if line:  # skip empty rows
...                     try:
...                         values.append(float(line))
...                     except ValueError:
...                         print(f"Skipping invalid value: {line}")
...     except FileNotFoundError:
...         print(f"File '{PFilename}' not found.")
...     return values
... 
... def calculateSum(PValues: List[float]) -> float:
...     return round(sum(PValues), 1)
... 
... def calculateAverage(PValues: List[float]) -> float:
...     if len(PValues) == 0:
...         return 0.0
...     return round(sum(PValues) / len(PValues), 1)
SyntaxError: multiple statements found while compiling a single statement
