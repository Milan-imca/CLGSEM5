'''5
Write a temperature conversion function that converts Celsius to Fahrenheit. If the user inputs a
temperature below absolute zero (−273.15°C), raise a custom BelowAbsoluteZeroError. Catch and
handle this exception with a message indicating that the temperature is invalid.
'''

class BelowAbsoluteZeroError(Exception):
    pass

def celsius_to_fahrenheit(celsius):
    try:
        if celsius < -273.15:
            raise BelowAbsoluteZeroError("Temperature is below absolute zero (-273.15°C).")
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except BelowAbsoluteZeroError as e:
        return f"Error: {e}"


celsius = -300  
result = celsius_to_fahrenheit(celsius)
print(result)
