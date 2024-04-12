from utile import *  # Importe les fonctions utiles, peut-être des fonctions d'utilité pour le problème spécifique que tu traites
from random import randint  # Importe la fonction randint pour générer des nombres aléatoires

class AlgorithmeGenetique:
    def __init__(self, population=[], taillePopulation=0):
        self.population = population  # Liste des individus dans la population
        self.taillePopulation = taillePopulation  # Taille de la population
        self.fitness = [0 for i in range(taillePopulation)]  # Liste pour stocker les valeurs de fitness de chaque individu
        self.record = float('inf')  # Initialisation du record avec une valeur infinie (pour minimiser)
        self.distanceCourante = float('inf')  # Initialisation de la distance courante avec une valeur infinie
        self.meilleurIndividu = None  # Meilleur individu trouvé
        self.meilleurIndex = 0  # Index de l'individu le meilleur
        self.tauxMutation = 0.1  # Taux de mutation initialisé à 0.1 (10%)

    def calculerFitness(self, points):
        # Calcule la fitness de chaque individu dans la population
        for i in range(self.taillePopulation):
            individu = []
            for j in self.population[i]:
                individu.append(points[j])  # Crée une liste des points pour chaque individu
            distance = sommeDistances(individu)  # Calcule la somme des distances pour cet individu
            if distance < self.distanceCourante:
                self.meilleurIndividu = self.population[i]  # Met à jour le meilleur individu trouvé
            if distance < self.record:
                self.record = distance  # Met à jour le record si une distance plus courte est trouvée
                self.meilleurIndividu = self.population[i]  # Met à jour le meilleur individu trouvé
                self.meilleurIndex = i  # Met à jour l'index du meilleur individu
            self.fitness[i] = 1 / (distance + 1)  # Calcule la fitness pour cet individu
        self.normaliserFitness()  # Normalise les valeurs de fitness

    def normaliserFitness(self):
        # Normalise les valeurs de fitness pour qu'elles soient dans la plage [0, 1]
        somme = 0
        for i in range(self.taillePopulation):
            somme += self.fitness[i]  # Calcule la somme de toutes les valeurs de fitness
        for i in range(self.taillePopulation):
            self.fitness[i] = self.fitness[i] / somme  # Normalise chaque valeur de fitness

    def muter(self, genes):
        # Mutate les gènes avec une certaine probabilité (définie par le taux de mutation)
        for i in range(len(self.population[0])):
            if(randint(0, 100) / 100 < self.tauxMutation):  # Vérifie si la mutation se produit
                indexA = randint(0, len(genes) - 1)  # Choix aléatoire du premier index
                indexB = randint(0, len(genes) - 1)  # Choix aléatoire du deuxième index
                genes[indexA], genes[indexB] = genes[indexB], genes[indexA]  # Échange des gènes

    def croisement(self, genes1, genes2):
        # Effectue le croisement entre deux ensembles de gènes
        debut = randint(0, len(genes1) - 1)  # Point de début du croisement
        fin = randint(debut - 1, len(genes2) - 1)  # Point de fin du croisement
        try:
            fin = randint(debut + 1, len(genes2) - 1)  # Vérifie si le point de fin est valide
        except:
            pass
        nouveauxGenes = genes1[debut:fin]  # Sélectionne les gènes entre le début et la fin
        for i in range(len(genes2)):
            p = genes2[i]
            if p not in nouveauxGenes:
                nouveauxGenes.append(p)  # Ajoute les gènes de genes2 qui ne sont pas déjà présents
        return nouveauxGenes

    def selectionNaturelle(self):
        # Effectue la sélection naturelle pour créer une nouvelle population
        nouvellePopulation = []
        for i in range(self.taillePopulation):
            parent1 = selectionnerParent(self.population, self.fitness)  # Sélectionne le premier parent
            parent2 = selectionnerParent(self.population, self.fitness)  # Sélectionne le deuxième parent
            genes = self.croisement(parent1, parent2)  # Croise les gènes des parents
            self.muter(genes)  # Mutation des gènes
            nouvellePopulation.append(genes)  # Ajoute les gènes à la nouvelle population
        self.population = nouvellePopulation  # Met à jour la population avec la nouvelle population
