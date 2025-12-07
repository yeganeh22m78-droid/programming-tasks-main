Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... 
... print("Program starting.")
... print("This is a program with simple menu, where you can choose which operation the program performs.")
... 
... name = input("Before the menu, please insert your name: ")
... 
... while True:
... 
...     print("\nOptions:")
...     print("1 - Print welcome message")
...     print("0 - Exit")
...     
... 
...     choice = input("Your choice: ")
...     
...     # Perform action based on choice
...     if choice == "1":
...         print(f"Welcome {name}!")
...     elif choice == "0":
...         print("Exiting...")
...         break
...     else:
...         print("Unknown option.")
... 
... print("Program ending.")
