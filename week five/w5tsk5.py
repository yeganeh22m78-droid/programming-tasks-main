def main():
    print("Program starting.")
    Word = ""  # Initialize memory
    
    while True:
        print("\nOptions:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            Word = input("Insert word: ")
        elif choice == "2":
            print(f'Current word - "{Word}"')
        elif choice == "3":
            print(f'Word reversed - "{Word[::-1]}"')
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option")
    
    print("\nProgram ending.")

main()
