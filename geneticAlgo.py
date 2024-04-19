from utile import *  # Importe les fonctions utiles, peut-être des fonctions d'utilité pour le problème spécifique que tu traites
import random  # Importe la fonction randint pour générer des nombres aléatoires
import itertools

class AlgorithmeGenetique:
    
    def __init__(self, taillePopulation):
        
        self.population =[]  # Liste des individus dans la population
        self.taillePopulation = taillePopulation  # Taille de la population
        self.fitness = {}
        self.tauxDeMutation=0.015
        self.tauxElitisme= 0.3
        self.meilleurIndiv= None
        self.meilleurfitness=0




    
    #algo de selectioN par roulette
    def SelectionRoulette(self, coordonnee):

    # Calcule la fitness de chaque individu dans la population
        self.fitness={}
        fitnessCumu = {} #fitness cumuative de chaque individu
        fitnessC=0 #somme fitness cumulative
        
        for individu in self.population:
                
            distance = sommeDistances(individu,coordonnee)  # Calcule la somme des distances pour cet individu
            fitness = 1 / (distance + 1)  # Calcule la fitness pour cet individu
            self.fitness[tuple(individu)]= fitness # Ajoute la fitness au dictionnaire des fitness pour chaque individu
            """print("fitness de",individu,"est :", fitness)"""

        for individu,fit in self.fitness.items():

            if fit>= self.meilleurfitness:
                self.meilleurfitness = fit
                self.meilleurIndiv = individu
        print("la meilleur solution est; ", self.meilleurIndiv,"sa fitness est : ",self.meilleurfitness)
    

        #calcule la somme des fitnessCumulative pour chaque individu, derniere valeur est la somme de toutes les fitness de la pop
        for individu, fit in self.fitness.items():
            fitnessC+= fit
            fitnessCumu[tuple(individu)]= fitnessC
        """print("fitnesscumu = ",fitnessCumu)"""

        #normaliser la fitness
        fitNormalized = normaliser(fitnessCumu,fitnessC)
         
        
        #generer un nombre aléatoire entre 0 et 1 puis choisir l'indiv pour lequel la sommeCumu depasse Nbgenere
        #répété jusqu'a avoir le nb d'individu demandé (on choisi la moitier de taillepopulation)
        parentSelec=[]
        for i in range(self.taillePopulation//2):
            Nbgenere= random.uniform(0,1)
            """print("nb generé" ,i , " :",Nbgenere)"""
            for individu, fitnorm in fitNormalized.items():
            
                if fitnorm > Nbgenere:
                    parentSelec.append(individu)
                    break
        
        """print("les parents selectionnés sont: ", parentSelec)"""

        # Liste pour stocker les enfants générés
        children = []

        # Vérifier si le nombre de parents est impair
        if len(parentSelec) % 2 != 0:
            # Si le nombre de parents est impair, ajoutez le dernier parent à la descendance sans croisement
            children.append(list(parentSelec[-1]))
            # Enlevez le dernier parent de la liste des parents pour éviter de l'inclure dans d'autres croisements
            parentSelec = parentSelec[:-1]

        # Parcourir chaque combinaison unique de parents et effectuer le croisement
        for parent1, parent2 in itertools.combinations(parentSelec, 2):
            child1, child2 = crossover(list(parent1), list(parent2))
            children.append(list(child1))
            children.append(list(child2))

        # Afficher les enfants générés
        """for child in children:
            print("its a child ", child)"""

        children= self.mutation(children)
        """for child in children:
            print("its a MUTCHILD ", child)"""
        return children
    
    def elitist_replacement(self,children):

        sortedpoplist=[]
        # Triez les individus en fonction de leur fitness
        sortedpoptuple= sorted(self.fitness.keys(), key=lambda x: self.fitness[x], reverse=True)

        for indiv in sortedpoptuple:
            sortedpoplist.append(list(indiv))

        # Calcul du nombre d'individus à conserver en fonction du ratio d'élitisme
        elitism_count = int((len(sortedpoplist)) * self.tauxElitisme)
    
        # Sélection des meilleurs individus à conserver dans la nouvelle population
        new_population =  sortedpoplist[:elitism_count]
    
        # Ajout des enfants générés à la nouvelle population
        new_population.extend(children[:len(self.population) - elitism_count])
        self.population= new_population
        """print("nouvelle pop : ", self.population)"""
    
    


    def mutation(self,children):
    # Parcourir chaque ville dans l'enfant et appliquer la mutation avec une probabilité donnée par mutation_rate
        for i in range(len(children)):

         if random.random() < self.tauxDeMutation:
            # Choisir une autre ville aléatoire et l'échanger avec la ville actuelle pour la mutation
            j = random.randint(0, len(children) - 1)
            children[i], children[j] = children[j], children[i]
    
        return children


    #prend le nombre de ville entrée dans l'interface et une taile de population
    def initialize_population(self,nbVille): 
    
        for i in range(self.taillePopulation):#initialise la population avec des individu aléatoire,un individu un parcours représenté par une liste de ville
            individual = list(range(nbVille))#creer un individu
            random.shuffle(individual)#mélange la liste aléatoirement pour avoir des individu différents
            self.population.append(individual)#ajoute l'individu à la population
    
        




   
