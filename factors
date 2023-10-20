#!/usr/bin/python3
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollards_rho(n):
    def f(x):
        return (x**2 + 1) % n

    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None
    return d

def factorize(number):
    factors = []
    while number > 1:
        divisor = pollards_rho(number)
        if divisor is None:
            factors.append(number)
            break
        factors.append(divisor)
        number //= divisor
    return factors
