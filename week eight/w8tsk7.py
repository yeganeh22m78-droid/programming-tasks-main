# File: A8_T7.py
# Simple menu program to draw squares, circles and hexagons
# Written in a basic student style

import math
import svgwrite
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(dwg):
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))
    print("Square added.")

def drawCircle(dwg):
    print("Insert circle")
    cx = int(input("- Center X: "))
    cy = int(input("- Center Y: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))
    print("Circle added.")

def drawHexagon(dwg):
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    r = int(input("Apothem length: "))  # inradius
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # circumradius R
    R = r / math.cos(math.radians(30))

    # angles for 6 corners
    angles = [30, 90, 150, 210, 270, 330]
    points = []
    for a in angles:
        x = cx + R * math.cos(math.radians(a))
        y = cy - R * math.sin(math.radians(a))
        points.append((round(x), round(y)))

    dwg.add(Polygon(points=points, fill=fill, stroke=stroke))
    print("Hexagon added.")

def saveSvg(dwg):
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        dwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")

def showOptions():
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def main():
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        showOptions()
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            drawSquare(dwg)
        elif choice == 2:
            drawCircle(dwg)
        elif choice == 3:
            drawHexagon(dwg)
        elif choice == 4:
            saveSvg(dwg)
        else:
            print("Invalid choice.")

    print("Program ending.")

if __name__ == "__main__":
    main()
