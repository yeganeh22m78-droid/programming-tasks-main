def save_lines(lines):
    filename = input("Insert filename: ")
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + "\n")
        print(f"Lines saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")

print("Program starting.\n")

lines = []

try:
    while True:
        print("Options:")
        print("1 - Insert line")
        print("2 - Save lines")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            text = input("Insert text: ")
            lines.append(text)
        elif choice == "2":
            if lines:
                save_lines(lines)
            else:
                print("No lines to save.")
        elif choice == "0":
            if lines:
                save_choice = input("You have unsaved lines. Save before exit(y/n)?: ").lower()
                if save_choice == "y":
                    save_lines(line_
