import numpy as np
import pandas as pd

#Problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def problem10(n):
    
    x = 3
    primes = [2]
    while x < n:
        if all(x % i == 0 for i in primes):
        primes.append(x)
        x += 2
    return sum(primes)

problem10(2e6)