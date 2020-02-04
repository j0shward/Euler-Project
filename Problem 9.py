import numpy as np
import pandas as pd

#problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#a < b < c

#a^2 + b^2 = c^2

#a + b + c = 1000

for c in range(1,100000):
    for b in range(1,c):
        for a in range(1,b):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a=",a,"b=",b,"c=",c,"product=",a*b*c)
                break

