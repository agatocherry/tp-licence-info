from os import system
from time import sleep

def uneEtape(tab):
    print("len :", len(tab))
    if len(tab) < 2:
        return []
    newTab = []
    newTab.append(tab[1])
    for i in range(1, len(tab) - 1):
        if tab[i - 1] == 0 and tab[i + 1] == 0:
            newTab.append(0)
        elif tab[i - 1] == 1 and tab[i + 1] == 1:
            newTab.append(1)
        else:
            newTab.append(tab[i])
    newTab.append(tab[len(tab) - 2])
    return newTab

# print(uneEtape([1,1,1,0,0,0,1,1,1,0,0,0]))
# print(uneEtape([1,0,1,0,1,0,1,0,1,0,1,0]))
# print(uneEtape([0,0,0,1,0,1,0,1,0,1,0,1]))
# print(uneEtape([0,1,0,1,0,1,0,1,0,1,0,1,1]))

def afficheLigne (tab):
    system("clear")
    for i in tab:
        if i == 1:
            print("\u2588", end="")
        else:
            print("", end="")
    print()
    sleep(0.0750)

# afficheLigne(uneEtape([1,1,1,0,0,0,1,1,1,0,0,0]))
# afficheLigne(uneEtape([1,0,1,0,1,0,1,0,1,0,1,0]))
# afficheLigne(uneEtape([0,0,0,1,0,1,0,1,0,1,0,1]))
# afficheLigne(uneEtape([0,1,0,1,0,1,0,1,0,1,0,1,1]))

def simulation(tab):
    previous = []
    i = len(tab)
    while previous != tab:
        afficheLigne(tab)
        tab = uneEtape(tab)
        previous = uneEtape(tab)
    afficheLigne(tab)

# simulation([1,1,1,0,0,0,1,1,1,0,0,0])
# # simulation([1,0,1,0,1,0,1,0,1,0,1,0]) 
# simulation([0,0,0,1,0,1,0,1,0,1,0,1])
# simulation([0,1,0,1,0,1,0,1,0,1,0,1,1])
# simulation([1,0,1,0,1,0,1,0,1,0,1,0,0])
simulation([1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
# simulation([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
# simulation([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1])