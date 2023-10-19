#!/usr/bin/python3
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard_rho(n):
    def f(x):
        return (x ** 2 + 1) % n

    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    if d == n:
        return None
    return d

def prime_factors(n):
    factors = []
    while n > 1:
        factor = pollard_rho(n)
        if factor:
            factors.append(factor)
            n //= factor
        else:
            factors.append(n)
            break
    return factors

def main(input_file):
    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        n = int(number)
        factors = prime_factors(n)
        print(f"{n}={'*'.join(map(str, factors))}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
