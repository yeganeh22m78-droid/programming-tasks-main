print("Program starting.")

# Ask user for first and last name
first_name = input("Insert first name: ")
last_name = input("Insert last name: ")

# Ask user for filename
filename = input("Insert filename: ")

# Write the names to the file
with open(filename, "w") as file:
    file.write(first_name + "\n")
    file.write(last_name + "\n")
    file.write("\n")  # empty row at the end

print("Program ending.")
