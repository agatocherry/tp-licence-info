# Exercice 4. Alpine. [941.Valid Mountain Array] 
# Étant donnée une liste L d'entiers, écrire la fonction alpine qui retourne True si L est alpine et False sinon. 
# Une liste L est alpine si et seulement si : sa longueur est au moins 3 et il existe un i 
# tel que 0<i<len(L)-1 et L[0] < L[1] < ... < L[i - 1] < L[i] et L[i] > L[i + 1] > ... > L[len(L) - 1]

def alpine(L):
    if len(L) < 3:
        return False
    i = 0
    while i + 1 < len(L) and L[i] < L[i + 1]:
        i += 1
    if i == 0 or i == len(L) - 1:
        return False
    while i + 1 < len(L) and L[i] > L[i + 1]:
        i += 1
    return i == len(L) - 1

print(alpine([2,1])) # False
print(alpine([3,5,5])) # False
print(alpine([0,3,2,1])) # True
print(alpine([1,3,2])) #True