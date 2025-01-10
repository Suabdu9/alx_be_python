FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
converted_temp = 0

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32))
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32)
    return fahrenheit

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
