def estPair(nb):
    if nb > 10 or nb < -10:
        estPair(nb/10)
    if nb % 2 == 1:
        return False
    else:
        return True

print(estPair(50))
print(estPair(55))