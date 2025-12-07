import sys

print("Program starting.")

# Prompt user for exit code
exit_code_input = input("Insert exit code(0-255): ")

try:
    exit_code = int(exit_code_input)
    if exit_code < 0 or exit_code > 255:
        print("Error: Exit code must be between 0 and 255.")
        sys.exit(1)
except ValueError:
    print("Error: Invalid integer value.")
    sys.exit(1)

# Print message before exiting
print("Clean exit")

# Exit with the user-defined code
sys.exit(exit_code)
