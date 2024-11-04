from os import system
from time import sleep

def uneEtape(tab):
    print("len :", len(tab))
    if len(tab) < 2:
        return []
    newTab = []
    i = 1
    if tab[0] != tab[i]:
        newTab.append(tab[i])
    while i < len(tab)-1:
        if tab[i - 1] and tab[i + 1] == 0:
            newTab.append(0)
        elif tab[i - 1] and tab[i + 1] == 1:
            newTab.append(1)
        else:
            newTab.append(tab[i])
        i += 1
    if tab[i] != tab[i - 1] :
        newTab.append(tab[i - 1])
    return newTab
    
print(uneEtape([1,1,1,0,0,0,1,1,1,0,0,0]))
print(uneEtape([1,0,1,0,1,0,1,0,1,0,1,0]))
print(uneEtape([0,0,0,1,0,1,0,1,0,1,0,1]))
print(uneEtape([0,1,0,1,0,1,0,1,0,1,0,1,1]))

def afficheLigne (tab):
    # system("clear")
    for i in tab:
        if i == 1:
            print("\u2588")
        elif i == 0:
            print(" ")
    sleep(0.5)

afficheLigne(uneEtape([1,1,1,0,0,0,1,1,1,0,0,0]))
afficheLigne(uneEtape([1,0,1,0,1,0,1,0,1,0,1,0]))
afficheLigne(uneEtape([0,0,0,1,0,1,0,1,0,1,0,1]))
afficheLigne(uneEtape([0,1,0,1,0,1,0,1,0,1,0,1,1]))