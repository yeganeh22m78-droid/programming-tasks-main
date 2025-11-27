print("Program starting.")
print("This program can copy a file.")

# Ask user for source and destination filenames
source_file = input("Insert source filename: ")
destination_file = input("Insert destination filename: ")

try:
    # Read content from source file
    print(f"Reading file '{source_file}' content.")
    with open(source_file, "r") as file:
        content = file.read()
    print("File content ready in memory.")

    # Write content to destination file
    print(f"Writing content into file '{destination_file}'.")
    with open(destination_file, "w") as file:
        file.write(content)

    print("Copying operation complete.")

except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")

print("Program ending.")
