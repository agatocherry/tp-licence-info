# Exercice 3. Monotone. [896. Monotonic Array] 
# Une liste L d'entiers est dite monotone si, pour tout i<=j, L[i]<=L[j] ou si, pour tout i<=j, L[i]>=L[j]. Étant donnée une liste d'entiers L, écrire la fonction monotone qui retourne True si L est monotone et False sinon. Exemples :

def monotone(L):
    max = 0
    min = 0
    if len(L) == 0:
        return True
    if len(L) >= 2:
        if L[0] >= L[1]:
            for i in range(len(L) - 1):
                if L[i] >= L[i + 1]:
                    max += 1
        if  L[0] <= L[1]:
            for i in range(len(L) - 1):
                if L[i] <= L[i + 1]:
                    min += 1
                    print(L[i],"<=",L[i+1])
    print(max, len(L))
    if max != len(L)-1 and min != len(L)-1:
        return False
    return True
    


print(monotone([1,1,2])) # True
# print(monotone([2,3,3,4])) # True
# print(monotone([5,3,2,2])) # True
# print(monotone([1,3,2])) # False
# print(monotone([2,2,2,2,2])) # True
# print(monotone([2,2,2,4,3])) # False
# print(monotone([1, 2, 3, 4, 5])) # True, liste strictement croissante
# print(monotone([5, 4, 3, 2, 1])) # True, liste strictement décroissante
# print(monotone([1, 1, 1, 1, 1])) # True, liste constante
# print(monotone([1, 2, 2, 3, 4])) # True, liste croissante avec répétitions
# print(monotone([4, 3, 3, 2, 1])) # True, liste décroissante avec répétitions
# print(monotone([1, 3, 2, 4, 5])) # False, liste non monotone
# print(monotone([5, 3, 4, 2, 1])) # False, liste non monotone
# print(monotone([1])) # True, liste avec un seul élément
# print(monotone([])) # True, liste vide
# print(monotone([1, 2, 3, 2, 1])) # False, liste non monotone