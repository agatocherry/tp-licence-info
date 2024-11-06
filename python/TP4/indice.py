# Exercice 8. Indice. [leetcode :  28. Find the Index of the First Occurrence in a String] 
# Étant données deux chaînes de caractères s et t, écrire la fonction indice qui renvoie l'indice de la première occurrence de t dans s et -1 si t n'apparait pas dans s.

def indice(s, f):
    for i in range(len(s)):
        if s[i] == f[0]:
            find = 0
            for j in range(len(f)):
                if i+j < len(s) and s[i+j] == f[j]:
                    find += 1
            if find == len(f):
                return i
    return -1

print(indice('yessadbutsad','sad')) #3
print(indice('yessadbutsad','so')) #-1
