import copy
import time
from typing import Callable

# Function to read dataset values from a file
def readValues(PValues: list[int|float], filename: str) -> None:
    PValues.clear()  # Ensure no duplicate data
    try:
        with open(filename, 'r') as file:
            for line in file:
                value = int(line.strip())  # Convert line to integer
                PValues.append(value)
        print(f"Dataset '{filename}' loaded successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Error: Dataset contains non-integer values.")

# Bubble Sort implementation
def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n):
        for j in range(0, n-i-1):
            if PNums[j] > PNums[j+1]:
                PNums[j], PNums[j+1] = PNums[j+1], PNums[j]
    return PNums

# Quick Sort implementation
def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums)//2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# Function to measure sorting time in nanoseconds
def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    startTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    endTime = time.perf_counter_ns()
    elapsedTime = endTime - startTime
    return elapsedTime

# Function to save results to a file
def saveResults(results: list[str], filename: str
