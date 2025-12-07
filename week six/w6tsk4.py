print("Program starting.")
print("This program analyses a list of names from a file.")


filename = input("Insert filename to read: ")

try:
    print(f'Reading names from "{filename}".')
    names = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip() 
            if line:
                parts = line.split(";")
                for name in parts:
                    if name.strip():  
                        names.append(name.strip())

    
    print("Analysing names...")
    name_count = len(names)
    if name_count > 0:
        shortest_name_len = min(len(name) for name in names)
        longest_name_len = max(len(name) for name in names)
        average_name_len = sum(len(name) for name in names) / name_count
    else:
        shortest_name_len = longest_name_len = average_name_len = 0

    print("Analysis complete!")

    print("#### REPORT BEGIN ####")
    print(f"Name count - {name_count}")
    print(f"Shortest name - {shortest_name_len} chars")
    print(f"Longest name - {longest_name_len} chars")
    print(f"Average name - {average_name_len:.2f} chars")
    print("#### REPORT END ####")

except FileNotFoundError:
    print(f'Error: The file "{filename}" does not exist.')

print("Program ending.")
