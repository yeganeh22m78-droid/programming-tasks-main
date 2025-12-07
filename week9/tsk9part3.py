import sys
import os

print("Program starting.")

# Prompt user for filename
filename = input("Insert filename: ")

# Check if file exists
if not os.path.isfile(filename):
    print(f"Error! File '{filename}' does not exist.")
    sys.exit(1)

# Read and print file content
print(f"## {filename} ##")
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')  # Preserve line breaks
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)
print(f"\n## {filename} ##")

print("Program ending.")
