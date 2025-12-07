Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Enter "help" below or click "Help" above for more information.# A3_T4 More Menu Options
... 
... print("Program starting.")
... print("This is a program with simple menu, where you can choose which operation the program performs.")
... 
... name = input("Before the menu, please insert your name: ")
... 
... while True:
...     # Display menu
...     print("\nOptions:")
...     print("1 - Print welcome message")
...     print("2 - Print the name backwards")
...     print("3 - Print the first character")
...     print("4 - Show the amount of characters in the name")
...     print("0 - Exit")
...     
...     # Get user choice
...     choice = input("Your choice: ")
...     
...     # Perform action based on choice
...     if choice == "1":
...         print(f"Welcome {name}!")
...     elif choice == "2":
...         name_backwards = name[::-1]
...         print(f'Your name backwards is "{name_backwards}"')
...     elif choice == "3":
...         first_char = name[0]
...         print(f'The first character in name "{name}" is "{first_char}"')
...     elif choice == "4":
...         name_length = len(name)
...         print(f'There are {name_length} characters in the name "{name}"')
...     elif choice == "0":
...         print("Exiting...")
...         break
...     else:
...         print("Unknown option.")
... 
... print("Program ending.")
