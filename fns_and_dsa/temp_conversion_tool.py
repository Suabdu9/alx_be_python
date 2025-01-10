FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
converted_temp = 0

def convert_to_celsius(fahrenheit):
    global converted_temp
    converted_temp = (FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32))
    return converted_temp

def convert_to_fahrenheit(celsius):
    global converted_temp
    converted_temp = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32)
    return converted_temp

temperature = float(input("Enter the temperature to convert: "))
specification = input("Is this temperature in celsius or fahrenheit? (C/F): ")
if specification == "C":
    convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
elif specification == "F":
    convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    print("Incorrect input!")
