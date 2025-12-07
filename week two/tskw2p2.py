Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # This program asks for a car brand and model
... # Then prints them using two print commands with sep and end parameters
... 
... print("Program starting.")
... 
... # Ask for user input
... brand = input("Insert car brand: ")
... model = input("Insert car model: ")
... 
... # First print uses sep to join text
... print("Car brand is", f"\"{brand}\"", sep=" ")
... 
... # Second print continues the sentence using end=
... print("and the model is", f"'{model}'.", sep=" ", end="\n")
... 
... print("Program ending.")
