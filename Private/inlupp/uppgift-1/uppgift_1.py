# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
    """
    Kontrollerar om ett heltal är udda eller jämnt.
    
    x: Ett heltal.
    True om x är udda, annars False.
    """
    return x % 2 != 0 # betyder att x är udda (resten är inte noll).

print(is_odd(5))  # Output: True 
print(is_odd(4))  # Output: False
print(is_odd(0))  # Output: False
print(is_odd(-3)) # Output: True
