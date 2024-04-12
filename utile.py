from math import sqrt  # Importe la fonction sqrt pour calculer la racine carrée
from random import uniform  # Importe la fonction uniform pour générer des nombres aléatoires dans une plage donnée

def Distance(a, b):
    # Calcule la distance entre deux points a et b dans un espace 2D
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def sommeDistances(points):
    # Calcule la somme des distances entre les points dans une liste de points
    s = 0
    for i in range(len(points)):
        # Calcule la distance entre chaque point et le point suivant dans la liste
        dist = Distance(points[i], points[(i + 1) % len(points)])
        s += dist  # Ajoute la distance à la somme totale
    return s

def selectionnerParent(liste, probabilites):
    # Sélectionne un parent de la liste en fonction des probabilités données
    index = 0
    r = uniform(0, 1)  # Génère un nombre aléatoire entre 0 et 1
    while r > 0:
        r -= probabilites[index]  # Réduit r par la probabilité de l'élément actuel
        index += 1
    index -= 1  # Retourne à l'indice précédent, car la boucle s'arrête lorsque r devient négatif
    return liste[index].copy()  # Retourne une copie de l'élément sélectionné pour éviter les effets de bord
