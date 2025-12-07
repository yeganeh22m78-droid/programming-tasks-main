import sys
import os

def showHelp() -> None:
    print("Usage: python {} <source_file> <destination_file>".format(sys.argv[0]))

def copyFile(src: str, dst: str) -> None:
    proceed = True
    if os.path.exists(dst):
        overwrite = input(f'Destination file "{dst}" exists. Overwrite? (y/n): ').lower()
        if overwrite != 'y':
            proceed = False
            print("Copy canceled by user.")
    if proceed:
        try:
            with open(src, 'r') as f_src, open(dst, 'w') as f_dst:
                for line in f_src:
                    f_dst.write(line)
            print(f'Copying file "{src}" to "{dst}".')
        except Exception as e:
            print(f"Error! Could not copy file: {e}")
            sys.exit(-1)

def main() -> None:
    print("Program starting.")
    
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        sys.exit(-1)
    
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    if not os.path.exists(src_file_
