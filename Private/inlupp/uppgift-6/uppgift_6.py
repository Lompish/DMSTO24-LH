# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.


def multiplication_table(n: int, limit: int) -> list[int]:
    """
    Genererar multiplikationstabellen för n upp till limit i en lista.
    
    n: Talet för vilket multiplikationstabellen skapas.
    limit: Det högsta multiplicerandet.
    return: En lista med multiplikationstabellen för n upp till limit.
    """
    return [n * i for i in range(1, limit + 1)]

print(multiplication_table(2, 5))  # Output: [2, 4, 6, 8, 10]
print(multiplication_table(4, 6))  # Output: [4, 8, 12, 16, 20, 24]
print(multiplication_table(5, 5))  # Output: [5, 10, 15, 20, 25]
print(multiplication_table(3, 3))  # Output: [3, 6, 9]
print(multiplication_table(8, 5))  # Output: [8, 16, 24, 32, 40]
