# File: A8_T6.py
# Simple menu-driven program for drawing SVGs
# Written in a student project style

import svgwrite
from svgwrite.shapes import Rect, Circle

def drawSquare(dwg: svgwrite.Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    # Add rectangle (square) to drawing
    dwg.add(Rect(insert=(x, y),
                 size=(side, side),
                 fill=fill,
                 stroke=stroke))
    print("Square added.")

def drawCircle(dwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X: "))
    cy = int(input("- Center Y: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    # Add circle to drawing
    dwg.add(Circle(center=(cx, cy),
                   r=r,
                   fill=fill,
                   stroke=stroke))
    print("Circle added.")

def saveSvg(dwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        # Save with pretty formatting (2 space indentation)
        dwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1

def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            drawSquare(dwg)
        elif choice == 2:
            drawCircle(dwg)
        elif choice == 3:
            saveSvg(dwg)
        else:
            print("Invalid choice. Please try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
