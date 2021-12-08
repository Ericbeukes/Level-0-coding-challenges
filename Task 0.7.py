def fahrenheit_to_celcius(celsius):
    fahrenheit = 32 + (celsius * 9/5)
    print('%0.2f Celsius is: %0.2f Fahrenheit' %(celsius,fahrenheit))

def celcius_to_fahrenheit(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    print('%0.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

fahrenheit_to_celcius(10)
celcius_to_fahrenheit(59)
