# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = 32 + (celsius * 9/5)
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = 5/9 * (fahrenheit - 32)
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))