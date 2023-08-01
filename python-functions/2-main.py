#!/usr/bin/env python3
convert_to_celsius = __import__('2-temperature').convert_to_celsius

def test_convert_to_celsius():
    # Test cases
    print(convert_to_celsius(100))
    print(convert_to_celsius(-40))
    print(convert_to_celsius(-459.67))
    print(convert_to_celsius(32))

if __name__ == "__main__":
    test_convert_to_celsius()