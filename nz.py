# PROBLEMA 1
def multiply(a,b):
    mul = 0
    for i in range(abs(a)):
        mul += b
    if abs(a) != a:
        mul = -mul
    return mul

print(multiply(5,-3))


# PROBLEMA 2
import functools

def maximum(array):
    return functools.reduce(lambda a,b: a if a>b else b, array)

print(maximum([1,4,3,2,3,-1]))


# PROBLEMA 3
def clean(array):
    no_zero = list(filter(lambda x: x != 0, array))
    return no_zero

print(clean([1,0,False,'papaya',False,3.14159]))


# PROBLEMA 4