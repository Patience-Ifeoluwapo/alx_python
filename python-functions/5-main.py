#!/usr/bin/env python3
is_prime = __import__('5-prime').is_prime

if __name__ == "__main__":
    print(is_prime(17))
    print(is_prime(15))
    print(is_prime(-5))
    print(is_prime(0))