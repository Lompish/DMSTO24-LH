# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers: list[int]) -> list[int]:
    """
    Filtrerar ut alla jämna tal från den givna listan.
    
    numbers: En lista med heltal.
    return: En lista med alla jämna tal.
    """
    return [num for num in numbers if num % 2 == 0]

# Exempelanvändning
print(filter_odd([1, 2, 3, 4, 5, 6, 7, 8]))             # Output: [2, 4, 6, 8]
print(filter_odd([11, 15, 19, 21, 25, 29]))             # Output: []
print(filter_odd([10, 20, 33, 42, 54, 56, 74, 75]))     # Output: [10, 20, 42, 54, 56, 74]
print(filter_odd([]))                                   # Output: []

