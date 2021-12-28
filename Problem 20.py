# Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


def factorial(x):
    return x*factorial(x-1) if x > 1 else 1


sum([int(str(factorial(100))[i]) for i in range(len(str(factorial(100))))])
