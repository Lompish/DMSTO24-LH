# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    """
    Räknar antalet ord i en given text.
    
    text: Texten som ska kontrolleras.
    return: Antalet ord i texten.
    """
    words = text.split()  # dela vid mellanslag för att få en lista med ord.
    return len(words) #  för att få antalet.


print(word_count("Hej! Jag heter Linda."))       # Output: 4
print(word_count(""))                            # Output: 0
print(word_count("Jag älskar julen så mycket.")) # Output: 5

