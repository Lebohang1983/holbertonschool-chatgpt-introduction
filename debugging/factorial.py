#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negaive numbers"
    result = 1 
    while n > 1:
            result *= n
            n -= 1
    return result

def main():
    if len(sys.argv) != 2:
        print("Please enter an integer")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    f = factorial(num)
    print(f)

if __name__ == "__main__":
    main()
