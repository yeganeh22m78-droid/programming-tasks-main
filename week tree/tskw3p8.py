# A3_T7 Decision Trees

print("Program starting.")
print("Testing decision structures.")

# Prompt user for an integer
value = int(input("Insert an integer: "))

while True:
    # Display menu
    print("\nOptions:")
    print("1 - In one multi-branched decision")
    print("2 - In multiple independent if-statements")
    print("0 - Exit")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        print("Using one multi-branched decision structure.")
        # Multi-branched decision (elif chain)
        if value >= 400:
            value += 44
        elif value >= 200:
            value += 22
        elif value >= 100:
            value += 11
        print(f"Result is {value}")
        break
        
    elif choice == "2":
        print("Using multiple independent if-statements.")
        # Independent if-statements
        result = value  # Use a separate variable to not overwrite original for clarity
        if result >= 400:
            result += 44
        if result >= 200:
            result += 22
        if result >= 100:
            result += 11
        print(f"Result is {result}")
        break
        
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Unknown option.")

print("Program ending.")
