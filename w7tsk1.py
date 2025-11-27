print("Program starting.")
print("Collect positive integers.")

# List to store collected integers
integers = []

while True:
    try:
        # Ask user for input
        num = int(input("Insert positive integer(negative stops): "))
        
        if num < 0:
            # Stop collecting if negative integer is entered
            break
        else:
            # Store positive integers
            integers.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Stopped collecting positive integers.")

# Display results
if integers:
    print(f"Displaying {len(integers)} integers:")
    for index, value in enumerate(integers):
        ordinal = index + 1
        print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
else:
    print("No integers to display.")

print("Program ending.")
