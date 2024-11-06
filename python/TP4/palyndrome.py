# Exercice 4. Palindrome. [leetcode : 125. Valid Palindrome] 
# Étant donnée une phrase (une chaîne de caractères), écrire la fonction estPalindrome qui retourne True si la phrase forme un palindrome (on convertit tous les caractères en minuscule, on supprime tous les symboles et tous les espaces) et False sinon. Exemple de script principal :

def isPalindrome(s):
        back = ""
        i = 0
        while i < len(s):
            if (s[i].isalpha() or s[i].isdigit()):
                if (s[i].isupper()):
                    back = s[i].lower() + back
                else :
                    back = s[i] + back
            i+=1
        front = ""
        i = 0
        while i < len(s):
            if (s[i].isalpha() or s[i].isdigit()):
                if (s[i].isupper()):
                    front = front + s[i].lower() 
                else :
                    front = front + s[i]
            i+=1
        if back == front:
            return True
        return False

phrase="a man, a plan, a canal: Panama !"
resultat=isPalindrome(phrase)
print(resultat)
print(isPalindrome("test"))
print(isPalindrome("testset"))