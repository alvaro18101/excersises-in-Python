# PROBLEMA 1
def multiply(a,b):
    mul = 0
    for i in range(abs(a)):
        mul += b
    if abs(a) != a:
        mul = -mul
    return mul

print(multiply(5,-3))


# 