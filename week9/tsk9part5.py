print("Program starting.")

try:
    # Collect RGB values
    r = int(input("Insert red: "))
    g = int(input("Insert green: "))
    b = int(input("Insert blue: "))
    
    # Check range
    if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
        raise ValueError("Value out of range")
    
    # Display RGB details
    print("RGB Details:")
    print(f"- Red {r}")
    print(f"- Green {g}")
    print(f"- Blue {b}")
    print(f"- Hex #{r:02x}{g:02x}{b:02x}")

except Exception:
    print("Couldn't perform the designed task due to the invalid input values.")

print("Program ending.")
