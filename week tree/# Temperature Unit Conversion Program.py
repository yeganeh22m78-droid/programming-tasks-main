# Temperature Unit Conversion Program

print("Program starting.\n")

# Display menu
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

# Get user choice
choice = input("Your choice: ")

if choice == "1":
    # Celsius to Fahrenheit
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F")

elif choice == "2":
    # Fahrenheit to Celsius
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C")

elif choice == "0":
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")
