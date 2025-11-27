print("Program starting.")

input_str = input("Insert comma separated integers: ")

values = input_str.split(",")

valid_integers = []

for val in values:
    val = val.strip()  
    if val:  
        try:
            number = int(val)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value detected: '{val}'")

# Analyse the valid integers
if valid_integers:
    total_count = len(valid_integers)
    total_sum = sum(valid_integers)
    sum_type = "even" if total_sum % 2 == 0 else "odd"

    print(f"There are {total_count} integers in the list.")
    print(f"Sum of the integers is {total_sum} and it's {sum_type}")
else:
    print("No valid integers to analyse.")

print("Program ending.")
