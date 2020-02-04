import numpy as np
import pandas as pd


#problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
#without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

p = 1
for i in range(1,1000000000):
    if all(i % j == 0 for j in range(1,21)):
        print(i)
        break