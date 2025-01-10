# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers: list) -> int:
    """
    Beräknar summan av alla siffror i listan.
    
    numbers: En lista med heltal eller decimaltal.
    return: Summan av alla siffror i listan.
    """
    return sum(numbers)


print(sum_list([1, 2, 3, 4]))        # Output: 10
print(sum_list([10, -5, 6]))         # Output: 11
print(sum_list([11.5,-5.5,15.5]))    # Output: 21.5
print(sum_list([]))                  # Output: 0
