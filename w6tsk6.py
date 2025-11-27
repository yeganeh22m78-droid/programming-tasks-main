Create a Python program which collects plain text rows from user till the user inserts an empty row. Cipher all rows and then ask user to choose between showing the ciphered text or saving it.

A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
N	O	P	Q	R	S	T	U	V	W	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M
Program must be able to cipher following lowercase and uppercase alphabets. Other characters remains same during ciphering operation.

# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Example program runs:

run 1 run 2 run 3 run 4
Program starting.

Collecting plain text rows for ciphering.
Insert row(empty stops): Hello
Insert row(empty stops): World
Insert row(empty stops): 

#### Ciphered text ####
Uryyb
Jbeyq

#### Ciphered text ####
Insert filename to save: A6_T6_F1.txt
Ciphered text saved!
Program ending.
