from math import sqrt  # Importe la fonction sqrt pour calculer la racine carrée
import random

# Calcule la distance entre deux points a et b dans un espace 2D
def Distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Calcule la somme des distances entre les villes dans une liste d'individus et les coordonnées des villes (dictionnaire)
def sommeDistances(individu, coordonnee):
    s = 0  #somme
    for i in range(len(individu)):
        # Calcule la distance entre chaque ville et la ville suivante dans l'individu
        ville_actuelle = individu[i]
        # Utilisation de l'opérateur modulo pour gérer le cas où nous sommes à la dernière ville
        ville_suivante = individu[(i + 1) % len(individu)]
        dist = Distance(coordonnee[ville_actuelle], coordonnee[ville_suivante])
        s += dist  # Ajoute la distance à la somme totale
    
    
    # Ajouter la distance entre la dernière et la première ville
    premiere_ville = individu[0]
    derniere_ville = individu[-1]
    
    s += Distance(coordonnee[derniere_ville], coordonnee[premiere_ville])
    """print("SommeDistance:",s)"""
    return s

#diviser la fitnessCumu de chaque individu par la somme des fitnessCumu de a pop pour avoir des probabilité de selection pour chaque indiv        
def normaliser(fitnessCumu,fitnessC):
    fitNormaliser = {}#individu et leur fitness normalisé
    for individu,fit in fitnessCumu.items():
        if fitnessC!=0:
            fitNormaliser[tuple(individu)]= fit/ (fitnessC)

    """for indiv,fitnorm in fitNormaliser.items():
        print("normaise : ",indiv,":", fitnorm)"""
    
    return fitNormaliser

#fonction de recombinaison
def crossover(parent1, parent2):
    # point de croisement aléatoire
    crossover_point = random.randint(1, len(parent1) - 1)  # Assurez-vous que le point de croisement n'est pas à l'extrémité

    # Créer des enfants en croisant les parents au point de croisement
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]

    return child1, child2


