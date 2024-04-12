from utile import *
from random import randint

class AlgorithmeGenetique:
    def __init__(self, population=[], taillePopulation=0):
        self.population = population
        self.taillePopulation = taillePopulation
        self.fitness = [0 for i in range(taillePopulation)]
        self.record = float('inf')
        self.distanceCourante = float('inf')
        self.meilleurIndividu = None
        self.meilleurIndex = 0
        self.tauxMutation = 0.1

    def calculerFitness(self, points):
        for i in range(self.taillePopulation):
            individu = []
            for j in self.population[i]:
                individu.append(points[j]) 
            distance = sommeDistances(individu)
            if distance < self.distanceCourante:
                self.meilleurIndividu = self.population[i]

            if distance < self.record:
                self.record = distance
                self.meilleurIndividu = self.population[i]
                self.meilleurIndex = i
            
            self.fitness[i] = 1/(distance+1)
        self.normaliserFitness()


    def normaliserFitness(self):
        somme = 0
        for i in range(self.taillePopulation):
            somme += self.fitness[i]
        for i in range(self.taillePopulation):
            self.fitness[i] = self.fitness[i]/somme
    
    def muter(self, genes):
        for i in range(len(self.population[0])): 
            if(randint(0,100)/100 < self.tauxMutation):
                indexA = randint(0,len(genes)-1)
                indexB = randint(0,len(genes)-1)
                genes[indexA], genes[indexB] = genes[indexB], genes[indexA]

    def croisement(self, genes1, genes2): 
        debut = randint(0,len(genes1)-1)
        fin = randint(debut-1,len(genes2)-1)
        try:
            fin = randint(debut+1, len(genes2)-1)
        except:
            pass
        nouveauxGenes = genes1[debut:fin]
        for i in range(len(genes2)): 
            p = genes2[i]
            if p not in nouveauxGenes: 
                nouveauxGenes.append(p)
        return nouveauxGenes
    
    def selectionNaturelle(self):
        nouvellePopulation = []
        for i in range(self.taillePopulation): 
            parent1 = selectionnerParent(self.population, self.fitness)
            parent2 = selectionnerParent(self.population, self.fitness)
            genes = self.croisement(parent1, parent2)
            self.muter(genes)
            nouvellePopulation.append(genes)
        self.population = nouvellePopulation

