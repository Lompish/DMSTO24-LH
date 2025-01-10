# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password: str) -> bool:

    """
    Kontrollerar om lösenordet är minst 8 tecken långt och innehåller en siffra.
    
    password: Lösenordet som ska kontrolleras.
    return: True om lösenordet följer krav, annars är det False.
    """
    if len(password) >= 8 and any(char.isdigit() for char in password):
        return True
    return False

print(validate_password("password"))            # Output: False saknar en siffra.
print(validate_password("p12345"))              # Output: False saknar 8 tecken. 
print(validate_password("safe1234"))            # Output: True följer kravet. 
print(validate_password("Catwithabighat123"))   # Output: True följer kravet. 
