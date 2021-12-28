# Euler Project - Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import numpy as np
import pandas as pd

ones = {"1": "One", "2": "Two", "3": "Three", "4": "Four",
        "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}

twos = {"1": "Ten", "2": "Twenty", "3": "Thirty", "4": "Forty",
        "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}

teens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen",
         "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}

length = 0

for x in range(1, 1001):
    x = str(x)
    if len(x) == 1:
        length += len(ones[x])
    if len(x) == 2:
        if x[0] == "1":
            length += len(teens[x])
        else:
            if x[1] == "0":
                length += len(twos[x[0]])
            else:
                length += len(twos[x[0]])
                length += len(ones[x[1]])
    if len(x) == 3:
        if x[1:] == "00":
            length += len(ones[x[0]])
            length += len("hundred")
        else:
            if x[2] == "0":
                length += len(ones[x[0]])
                length += len("hundredand")
                length += len(twos[x[1]])
            else:
                if x[1] == "0":
                    length += len(ones[x[0]])
                    length += len("hundredand")
                    length += len(ones[x[2]])
                elif x[1] == "1":
                    length += len(ones[x[0]])
                    length += len("hundredand")
                    length += len(teens[x[1:]])
                else:
                    length += len(ones[x[0]])
                    length += len("hundredand")
                    length += len(twos[x[1]])
                    length += len(ones[x[2]])
    if len(x) == 4:
        length += len("onethousand")
print(length)
