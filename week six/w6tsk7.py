import os
import codecs  # for ROT13 encoding/decoding

# Define locations
locations = [
    "home",
    "Galba's palace",
    "Otho's palace",
    "Vitellius' palace",
    "Vespasian's palace"
]

# Player progress file
progress_file = "player_progress.txt"

# Initialize progress file if it doesn't exist
if not os.path.exists(progress_file):
    with open(progress_file, "w") as f:
        f.write("current_location;next_location;passphrase\n")
        f.write("0;1;qvfpvcyvar\n")  # ROT13 for
