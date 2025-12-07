TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")
    
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception(f"{celsius} temperature out of range.")
    
    return celsius

print("Program starting.")

try:
    celsius = collectCelsius()
    print(f"You inserted {celsius} °C")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Exception: {e}")

print("Program ending.")
