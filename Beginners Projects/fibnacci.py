# methods to print nth Fibonacci number
from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#for i in range(41):
# i = 499
i = 10
print(f"{i}: {fib(i)}")


# math formula to find Fibonacci number
# import math #math.sqrt
#import math as m
#from math import (sqrt,cbrt)
from math import *
def fibonacci(n):
    sqrt5 = sqrt(5)
    phi = (1 + sqrt5) / 2
    return round((1 / sqrt5)*(phi**n - (1-phi)**n))

# i = 1474
i = 14
print(f"{i}: {fibonacci(i)}")

#method 2 # mathematically can find fibonacci no from 12 only
result = round(144*(1.618)**(i-12))
print(result)
