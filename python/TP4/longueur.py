# Exercice 10. Longueur. [58. Length of Last Word] 
# Étant donnée une chaîne de caractères (constituée uniquement de lettres et d'espaces), écrire la fonction longueur retournant le nombre de caractères du dernier  mot (non vide).

def longueur(s):
    i = len(s) - 1
    word = 0
    while s[i] and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] and s[i] != ' ':
        word += 1
        i -= 1
    return word

print(longueur("    fly    me to   the moon    ")) #4
print(longueur("a")) 