#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Argument must be an integer")
        sys.exit(1)
    if num < 0:
        print("Number must be >= 0")
        sys.exit(1)
    print(factorial(num))
