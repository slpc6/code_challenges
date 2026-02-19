"""Map and Lamda Functions"""

def fibonacci(n: int) -> list:
    """Return the fibonacci sequence"""
    fib = [0, 1]
    if n == 0:
        fib = []
    elif n == 1:
        fib = [0]
    else:
        while len(fib) < n:
            fib.append(fib[-1]+ fib[-2])
    return fib

if __name__ == '__main__':
    print(list(map(lambda x: pow(x, 3), fibonacci(int(input())))))
