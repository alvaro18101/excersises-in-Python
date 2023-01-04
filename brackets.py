def check(string):
    open = ['(','[','{']
    close = [')',']','}']
    push = []
    for i in string:
        if i in open:
            push.append(i)
        if i in close:
            if  push[-1] != open[close.index(i)]:
                return False
            else:
                push.pop(-1)
    return True

print(check('(())[()]'))
print(check('[()]{}{[()()]()}'))
print(check('[(])'))