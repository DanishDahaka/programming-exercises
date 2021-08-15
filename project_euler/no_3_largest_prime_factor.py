#!/bin/python3
import math

# adapted after example 1 from: https://www.pythonpool.com/prime-factorization-python/

def prime_factors(n) -> int:
    
    factors = []
    # even number divisible
    while n % 2 == 0:
        factors.append(2),
        n = n // 2

    # n is odd
    for i in range(3,int(math.sqrt(n))+1,2):
        
        while (n % i == 0):
            factors.append(i)
            n = n // i
            
    # append last value, e.g. 
    if n > 2:
        factors.append(n)

    return max(factors)

""" HackerRank input
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(prime_factors(n))"""

if __name__ == '__main__':

    nums = [10,17]

    for num in nums:
        print(prime_factors(num)) # returns 5 and 17

    
    