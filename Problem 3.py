import numpy as np
import pandas as pandas

#problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def max_prime_factor(n):
    x = []
    q = 2
    while n > 1:
        while n % q == 0:
            x.append(q)
            n = n/q
        q = q + 1

    return max(x)

max_prime_factor(600851475143)
