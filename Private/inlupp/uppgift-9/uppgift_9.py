# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string: str) -> bool:
    """
    Kontrollerar om en given sträng är ett palindrom.
    
    string: Strängen som ska kontrolleras.
    return: True om strängen är ett palindrom, annars False om den inte är det.
    """
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum()) # ta bort oönskade tecken som mellanslag, specialtecken och punkter. Använder bara bokstäver och siffror. 
    return cleaned_string == cleaned_string[::-1] # är strängen baklänges.


print(is_palindrome("Anna"))                # Output: True
print(is_palindrome("Linda"))               # Output: False 
print(is_palindrome("Ni talar bra latin!")) # Output: True
print(is_palindrome("12321"))               # Output: True
print(is_palindrome("56789"))               # Output: False