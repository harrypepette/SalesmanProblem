from utile import *
from algo_genetic import *
import tkinter as tk
import random


#creer un instance de notre classe algogenetic our initiaiser la taille de la population
AlgoG= AlgorithmeGenetique(50)#creer une instance d'algo genetique avec la taille de population souhaitée

################################ Fonctions Bouton #########################################################

# Action à effectuer lorsque le bouton "générer les villes" est cliqué
def G_Villes():
    
    number = entry1.get() # Récupérer le chiffre entré pour le nombre de ville
    print("Chiffre entré:", number)
    draw_villes(int(number)) # Appel de la fonction draw_villes pour dessiner les points
    update_label(int(number)) # Mettre à jour l'étiquette avec le nombre de villes

running = True

# Action à effectuer lorsque le bouton "Go" est cliqué
def go():
    global running
    if not running:
        return
    
    number = entry1.get() # Récupérer le le nombre de ville
    boucle= entry2.get()# pareile pour le nombre de boucle
    AlgoG.initialize_population(int(number))#initialiser la population



    #fonction defini dans Go pour pouvoir utiier root.after
    def run(iteration):
        global running
        if not running:# arreter l'algorithme grace au bouton stop et la variable globale running
            return
        
        #pour chaqu iteration tant qu'on ne depasse pas le boucle
        #on met à jour l'ieration, suprime le dessin de l'ancien meileur individu
        #on reapplique l'algorithme à roulette ,dessine le nouveau chemin 
        #puis remlace notre population par la nouvelle
        if iteration<int(boucle):
            update_label2(int(iteration))
            canvas.delete("path")
            children=AlgoG.SelectionRoulette(coordonnee)
            draw_path(AlgoG.meilleurIndiv)
            AlgoG.elitist_replacement(children)
            root.after(300,run,iteration+1)


        """for indiv,coo in coordonnee.items():
             print(indiv,":", coo)"""

        """for indiv in AlgoG.population:
             print("premièere pop" ,indiv)"""
        
    run(0)  

# Fonction pour arrêter l'algorithme génétique en cours d'exécution
def stop():
    
    global running
    running = False
    Label3.pack(side="bottom")
    Label3.config(text="Le meilleur individu est : {}".format(AlgoG.meilleurIndiv))
    

####################### Fonction de dessin ###########################################################
#dictionnaire des coordonnées des villes génére    
coordonnee={}

# Dessiner les points aléatoirement
def draw_villes(num_villes):
   
    for i in range(num_villes):
        x = random.randint(10, canvas.winfo_width() - 10)
        y = random.randint(10, canvas.winfo_height() - 10)

        #ajouter chaque coordonée au dico coordonnee
        coordonnee[i]=[x,y]
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")
        canvas.create_text(x, y - 10, text=str(i))


# Dessiner le chemin sur le canevas avec un trait
def draw_path(path):
   
    for i in range(len(path) - 1):
        x1, y1 = coordonnee[path[i]]
        x2, y2 = coordonnee[path[i + 1]]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=1,tags="path")

    #dessine a dernière ligne entre la dernière et première ville
    x1, y1= coordonnee[path[0]]
    x2, y2 = coordonnee[path[-1]]
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=1,tags="path") 


############################## Creation des Label,boutton et creation interface#######################

# Création de la fenêtre principale avec Tkinter
root = tk.Tk()
root.title("Interface graphique")
root.geometry("800x600")

# Création de l'étiquette pour la consigne du nombre de ville
label_consigne1 = tk.Label(root, text="Entrez un nombre de villes:",anchor="w")
label_consigne1.pack(side="top")

# Création de l'entry pour entrer un chiffre (nombre de ville)
entry1 = tk.Entry(root)
entry1.pack(side="top")

# Création de l'étiquette pour la consigne du nombre de boucle
label_consigne2 = tk.Label(root, text="Entrez un nombre de boucle:",anchor="w")
label_consigne2.pack(side="top")

entry2 = tk.Entry(root)
entry2.pack(side="top")

# Création de l'étiquette pour afficher le nombre de ville
label1 = tk.Label(root, text="Nombre de ville: 0")
label1.pack(side="bottom")

#au debut on affiche le nombre de boucle
label2= tk.Label(root, text="Nombre de boucle: 0")
label2.pack(side="bottom")

#meilleur individu
Label3=tk.Label(root,text="Le meilleur individu est :")

#fonctions de mise à jour d'etiquette
def update_label(num_points):
    label1.config(text="Nombre de villes: {}".format(num_points))

def update_label2(numboucle):
    label2.config(text="Numéro de la boucle : {}".format(numboucle))


# Création du bouton "Generer les villes"
genererVilles = tk.Button(root, text="Generer les villes", command=G_Villes)
genererVilles.pack()

# Création du bouton "Go"
go_button = tk.Button(root, text="Go", command=go)
go_button.pack()

# Création du bouton "Stop"
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side="top")

# Création du canevas pour dessiner les points
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack()

###############################Lancer la boucle principale#############################################

root.mainloop()
