# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:

    """
    Konverterar en temperatur från Celsius till Fahrenheit.
    
    celsius: Temperaturen i Celsius.
    return: Temperaturen i Fahrenheit.
    """
    return celsius * 9 / 5 + 32 # Formeln för att konvertera Celsius till Fahrenheit

print(celsius_to_fahrenheit(25))       # Output: 77.0
print(celsius_to_fahrenheit(-40))      # Output: -40.0 
print(celsius_to_fahrenheit(-50))      # Output: -58.0
print(celsius_to_fahrenheit(0))        # Output: 32.0 
print(celsius_to_fahrenheit(20))       # Output: 68.0 

