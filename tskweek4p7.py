print("Program starting.\n")

print("Check multiplicative persistence.")
number = input("Insert an integer: ")

steps = 0

# Continue until only one digit remains
while len(number) > 1:
    digits = list(number)
    
    # Print the multiplication step
    print(" * ".join(digits), end=" = ")
    
    # Multiply the digits
    product = 1
    for d in digits:
        product *= int(d)
    
    print(product)
    
    # Prepare for next loop
    number = str(product)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
