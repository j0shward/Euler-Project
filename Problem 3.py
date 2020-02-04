import numpy as np
import pandas as pd

#problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime_factor(n):
    q = []
    for i in range(1,n):
        if n % i == 0:
            if all(i % j != 0 for j in range(2, i)):    
                q.append(i)
    return max(q)

prime_factor(600851475143)