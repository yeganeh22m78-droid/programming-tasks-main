def askDimension(PPrompt: str) -> float:
    value = float(input(f"Insert {PPrompt}: "))
    return value

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = PWidth * PHeight
    return Area

def main():
    print("Program starting.")
    
    Width = askDimension("width")
    Height = askDimension("height")
    
    Area = calcRectangleArea(Width, Height)
    
    print(f"\nArea is {Area}²")
    print("Program ending.")

main()
