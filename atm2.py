def cash(n):
    if n%10 != 0:
        return False
    else:
        billetes = [200, 100, 50, 20, 10]
        array = []
        for i in billetes:
            array.append([n//i,i])
            n = n%i
    return array

print(cash(590))