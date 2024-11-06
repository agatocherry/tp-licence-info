# Exercice 9. Rang. [leetcode : 35. Search Insert Position] 
# Étant donnés une liste L d'entiers triés et un entier n, écrire la fonction rang retournant l'indice de n dan L si n est présent, 
# et l'indice d'insertion de n si n est non présent. Votre algorithme doit avoir une complexité en temps logarithmique (approche dichotomique).

def rang(L, n):
    for i in range(len(L)):
        if n == L[i]:
            return i
    for j in range(len(L)):
        if L[j] > n:
            return j
    return j+1

print(rang([1,2,5,7],5)) #2
print(rang([1,2,5,7],6)) #3