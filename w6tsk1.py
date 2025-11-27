Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Program starting.")
... print("This program can read a file.")
... 
... # Ask the user for the file name
... filename = input("Insert filename: ")
... 
... try:
...     # Open the file
...     file = open(filename, "r")
...     
...     # Print start decorative line
...     print(f'#### START "{filename}" ####')
...     
...     # Read and print each line
...     for line in file:
...         print(line, end='')  # end='' prevents extra blank lines
...     
...     # Print end decorative line
...     print(f'\n#### END "{filename}" ####')
...     
...     # Close the file
...     file.close()
...     
... except FileNotFoundError:
...     print(f'Error: The file "{filename}" was not found.')
... 
... print("Program ending.")
