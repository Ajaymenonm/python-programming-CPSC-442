## Write a Python program which prompts the user for a Celsius temperature, converts the temperature to Fahrenheit, and prints out the converted temperature.

print('Please enter the temperature in celsius')
celsius = input()
fahrenheit = round(((float(celsius) * 9) / 5 + 32), 2)
print("Temperature in Fahrenheit is " + str(fahrenheit))
