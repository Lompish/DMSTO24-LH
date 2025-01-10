# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string: str) -> dict[str, int]:
    """
    Räknar antalet förekomster av varje bokstav i en sträng.
    
    string: Strängen som ska kontrolleras.
    return: En dictionary med bokstäver som nycklar och antalet förekomster som värden.
    """
    count = {}
    for char in string:
        if char.isalpha():  # Kontrollera om tecknet är en bokstav
            char = char.lower()  # Gör bokstaverna i samma storlek
            count[char] = count.get(char, 0) + 1
    return count

print(count_letters("Jag är bäst!"))                   # Output: {'j': 1, 'a': 1, 'g': 1, 'ä': 2, 'r': 1, 'b': 1, 's': 1, 't': 1}
print(count_letters("Hello World!"))                   # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print(count_letters("Jag lär mig så mycket nytt!"))    # Output: {'j': 1, 'a': 1, 'g': 2, 'l': 1, 'ä': 1, 'r': 1, 'm': 2, 'i': 1, 's': 1, 'å': 1, 'y': 2, 'c': 1, 'k': 1, 'e': 1, 't': 3, 'n': 1}
print(count_letters(""))                               # Output: {}