import numpy as np
import pandas as pd

#problem 4
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
z = []
for i in range(1,1000):
    for j in range(1,1000):
        if int(str(i*j)[::-1]) == i*j:
            z.append(i*j)
max(z)