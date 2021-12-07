celsius = float(15)
fahrenheit = float(59)

def fahrenheit_to_celcius():
    fahrenheit = 32 + (celsius * 9/5)
    print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))



def celcius_to_fahrenheit():
    celsius = 5/9 * (fahrenheit - 32)
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

fahrenheit_to_celcius()
celcius_to_fahrenheit()