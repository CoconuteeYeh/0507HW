# -*- coding: utf-8 -*-
"""
Created on Tue May  2 00:26:43 2023

@author: Chih Tung
"""

import time
import matplotlib.pyplot as plt
from functools import lru_cache

#@lru_cache(maxsize=None)
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

# Measure the execution time of the recursive and dynamic programming implementations of Fibonacci numbers up to F(100)
# values of n to test
n_values = range(10, 101, 10)

# list to store execution times for recursive, dynamic programming implementation
recursive_times = []
dynamic_times = []


for n in range(10, 101, 10):
    if n < 50:
        start = time.time()
        fib_recursive(n)
        end = time.time()
        recursive_times.append(end - start)
    else:
        recursive_times.append(1000)  # Set a large value for execution time  

    
    # Measure execution time for dynamic programming implementation
    start_time = time.time()
    fib_dp(n)
    end_time = time.time()
    dynamic_times.append(end_time - start_time)
    print('F(', n, ') = ', fib_dp(n))

# Plot the results as a line chart
n_values = range(10, 101, 10)
plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel("Fibonacci Number (n)")
#plt.xticks(n_values, values)
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Fibonacci Algorithms')
plt.legend()
plt.show()