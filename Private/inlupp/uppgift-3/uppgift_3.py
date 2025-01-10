# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list[int]) -> int:
    """
    Hittar det största talet i en lista.

    numbers: En lista med heltal.
    return: Det största talet i listan.
    """
    return max(numbers)

print(max_in_list([56, 44, 67, 2, 555, 889])) # Output: 889
print(max_in_list([1, 2, 3, 4]))              # Output: 4
print(max_in_list([-10, -5, -3, -1]))         # Output: -1
print(max_in_list([100, 50, 150]))            # Output: 150
