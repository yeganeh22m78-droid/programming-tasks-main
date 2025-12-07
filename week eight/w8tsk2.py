# File: calculator_lib.py
# Arithmetic operations library

def add(PAddend1: float, PAddend2: float) -> float:
    return PAddend1 + PAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float:
    return PMinuend - PSubtrahend

def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    return PMultiplicant * PMultiplier

def divide(PDividend: float, PDivisor: float) -> float:
    if PDivisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return PDividend / PDivisor
