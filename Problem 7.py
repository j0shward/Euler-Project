import numpy as np
import pandas as pd

#problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

z = 1
prime = [2]
while len(prime) < 10001:
    z += 1
    if all(z % i == 0 for i in range(2, z)):
        prime.append(z)

prime[10000]