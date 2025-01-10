# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list[int]:
    """
    Genererar en lista med de första n Fibonacci-talen.
    
    param n: Antalet Fibonacci-tal att generera.
    return: En lista med de första n Fibonacci-talen.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(0))  # Output: []
print(fibonacci(1))  # Output: [0]
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(15)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
