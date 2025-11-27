import string

ALPHABET = string.ascii_uppercase

# Load rotor and reflector config from file
def load_config(filename):
    rotors = []
    reflector = ""
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            rotors.append(lines[0].split(":")[1].strip())
            rotors.append(lines[1].split(":")[1].strip())
            rotors.append(lines[2].split(":")[1].strip())
            reflector = lines[3].split(":")[1].strip()
    except FileNotFoundError:
        print(f"Config file {filename} not found.")
    return rotors, reflector

# Rotate rotors
def rotate_positions(positions):
    positions[0] += 1
    if positions[0] >= 26:
        positions[0] = 0
        positions[1] += 1
        if positions[1] >= 26:
            positions[1] = 0
            positions[2] += 1
            if positions[2] >= 26:
                positions[2] = 0

# Encrypt a single character
def encrypt_char(ch, rotors, reflector, positions):
    if ch not in ALPHABET:
        return ch  # Non-alphabet characters unchanged
    
    # Forward pass through rotors
    index = ALPHABET.index(ch)
    for i in range(3):
        index = (ALPHABET.index(rotors[i][index]) + positions[i]) % 26

    # Reflector
    ch_reflected = reflector[index]
    index = ALPHABET.index(ch_reflected)

    # Reverse pass through rotors
    for i in reversed(range(3)):
        rotor = rotors[i]
        idx_in_rotor = (rotor.index(ALPHABET[index]) - positions[i]) % 26
        index = idx_in_rotor

    return ALPHABET[index]

# Main program
print("Insert config(filename): ", end="")
config_file = input().strip()
rotors, reflector = load_config(config_file)

plug_input = input("Insert plugs (y/n)?: ").strip().lower()
if plug_input == "y":
    print("Plugboard not implemented in this demo.")
else:
    print("No extra plugs inserted.")

print("Enigma initialized.\n")

while True:
    row = input("Insert row (empty stops): ").strip().upper()
    if row == "":
        break

    positions = [0, 0, 0]  # Reset rotor positions
    converted_row = ""

    for ch in row:
        encrypted_ch = encrypt_char(ch, rotors, reflector, positions)
        print(f'Character "{ch}" illuminated as "{encrypted_ch}"')
        converted_row += encrypted_ch
        rotate_positions(positions)

    print(f"Converted row - \"{converted_row}\".\n")

print("Enigma closing.")
