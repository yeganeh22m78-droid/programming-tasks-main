print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

current = start
while current <= stop:
    if current < stop:
        print(current, end=" ")
    else:
        print(current)
    current += 1

print("\nProgram ending.")
