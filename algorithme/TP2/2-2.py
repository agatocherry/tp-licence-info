def existeMul11(a,b):
    if b == a:
        False
    elif a % 11 == 0:
        True
    else:
        existeMul11(a - 1, b)

print(existeMul11(2,10))
print(existeMul11(22,22))
print(existeMul11(22,2))