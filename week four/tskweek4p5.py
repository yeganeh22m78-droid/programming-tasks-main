print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

# Collecting possible errors
errors = []


if start >= stop:
    errors.append("Starting point value must be less than the stopping point value.")


if inspect <= start or inspect >= stop:
    errors.append("Inspection value must be within the range of start and stop.")

if len(errors) > 0:
    print()
    for e in errors:
        print(e)
else:
    print("\nFirst loop - inspection with break:")
    
    output1 = ""
    for i in range(start, stop):
        if i == inspect:
            break
        if output1 == "":
            output1 = str(i)
        else:
            output1 = output1 + " " + str(i)
    print(output1)

    print("Second loop - inspection with continue:")
    
    output2 = ""
    for i in range(start, stop):
        if i == inspect:
            continue
        if output2 == "":
            output2 = str(i)
        else:
            output2 = output2 + " " + str(i)
    print(output2)

print("\nProgram ending.")
