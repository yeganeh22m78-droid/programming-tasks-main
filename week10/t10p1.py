print("Program starting.")

# Prompt user for filename
filename = input("Insert filename: ")

# Initialize a list to store the file values
values = []

# Read file content
try:
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Ignore empty rows
                values.append(line)
except FileNotFoundError:
    print(f"Error! File '{filename}' not found.")
    print("Program ending.")
    exit(1)

# Display vertically
print("# --- Vertically --- #")
for value in values:
    print(value)
print("# --- Vertically --- #")

# Display horizontally
print("# --- Horizontally --- #")
print(", ".join(values))
print("# --- Horizontally --- #")

print("Program ending.")
