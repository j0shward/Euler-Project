import numpy as np
import pandas as pd

#problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

z = 3
primes = [2]
while len(primes) < 10001:
    if all(z % i == 0 for i in primes):
        primes.append(z)
    z += 2 #since we are starting with 3 and 2 is the only even prime    
primes[10000]
