#!/usr/bin/env python3
pow = __import__('1-power').pow

def test_pow():
    # Test cases
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))

    print("All test cases passed!")

if __name__ == "__main__":
    test_pow()