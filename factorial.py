import functools

factorial = lambda n: functools.reduce(lambda a,b: a*b,range(1,n+1))

print(factorial(5))
print(range(4)[3])