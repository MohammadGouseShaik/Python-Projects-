def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prompt the user to enter a temperature in Celsius or Fahrenheit
temp = float(input("Enter a temperature: "))
unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ")

# Convert the temperature and print the result
if unit.upper() == "C":
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
elif unit.upper() == "F":
    celsius = fahrenheit_to_celsius(temp)
    print(f"{temp} degrees Fahrenheit is {celsius} degrees Celsius.")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
