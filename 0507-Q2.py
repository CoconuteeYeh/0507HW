# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:50:17 2023

@author: Chih Tung
"""

# Recursive implementation
def fib_recursive(n):
    if n <= 1:
        return n
    elif n > 40: # set a threshold for n
        raise RecursionError("Maximum recursion depth exceeded")
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n = 0
while True:
    try:
        fib_recursive(n+1)
    except RecursionError:
        print("The maximum value of n for the recursive implementation is:", n)
        break
    print('Recursive:F(', n, ') =', fib_recursive(n))
    n += 1

# Dynamic programming implementation
def fib_dp(n):
    if n <= 1:
        return n

    # create a list to store the Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1

    # use dynamic programming to compute the Fibonacci numbers
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]

n = 0
while True:
    result = fib_dp(n+1)
    if result is None:
        print("The maximum value of n for the dynamic programming implementation is:", n)
        break
    print('Dynamic Programming:F(', n, ') =', fib_dp(n))
    n += 1