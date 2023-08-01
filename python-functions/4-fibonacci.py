#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence
if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))