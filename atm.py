def cash(n):
    if n%10 != 0:
        return False
    else:
        billetes = [200, 100, 50, 20, 10]
        array = []
        for i in billetes:
            while n>=i:
                n-=i
                array.append(i)
    return array

print(cash(590))