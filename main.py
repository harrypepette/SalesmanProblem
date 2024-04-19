from utile import *
from geneticAlgo import *
import tkinter as tk
import random




def G_Villes():
    # Action à effectuer lorsque le bouton "Go" est cliqué
    number = entry1.get() # Récupérer le chiffre entré dans l'entry
    boucle= entry2.get()
    # Insérer ici le traitement à effectuer avec le chiffre entré
    print("Chiffre entré:", number)
    draw_villes(int(number)) # Appel de la fonction pour dessiner les points
    update_label(int(number)) # Mettre à jour l'étiquette avec le nombre de points

running = True

def go():
    global running
    if not running:
        return
    # Action à effectuer lorsque le bouton "Go" est cliqué
    number = entry1.get() # Récupérer le chiffre entré dans l'entry
    boucle= entry2.get()
    AlgoG= AlgorithmeGenetique(50)#creer une instance d'algo genetique avec la taille de population souhaitée
    AlgoG.initialize_population(int(number))#initialiser la population




    def run(iteration):
        global running
        if not running:
            return
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
        
    
    
coordonnee={}

def draw_villes(num_villes):
    # Dessiner les points aléatoirement
    for i in range(num_villes):
        x = random.randint(10, canvas.winfo_width() - 10)
        y = random.randint(10, canvas.winfo_height() - 10)
        coordonnee[i]=[x,y]
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")
        canvas.create_text(x, y - 10, text=str(i))

def update_label(num_points):
    # Mettre à jour l'étiquette avec le nombre de points
    label1.config(text="Nombre de villes: {}".format(num_points))

def update_label2(numboucle):
    label2.config(text="Numéro de la boucle : {}".format(numboucle))
   

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface graphique")
root.geometry("800x600")

# Création de l'étiquette pour la consigne du nombre de ville
label_consigne1 = tk.Label(root, text="Entrez un nombre de villes:",anchor="w")
label_consigne1.pack(side="top")

# Création de l'entry pour entrer un chiffre
entry1 = tk.Entry(root)
entry1.pack(side="top")

# Création de l'étiquette pour la consigne du nombre de boucle
label_consigne2 = tk.Label(root, text="Entrez un nombre de boucle:",anchor="w")
label_consigne2.pack(side="top")

entry2 = tk.Entry(root)
entry2.pack(side="top")


def draw_path(path):
    # Dessiner le chemin sur le canevas avec un trait fin mais visible
    for i in range(len(path) - 1):
        x1, y1 = coordonnee[path[i]]
        x2, y2 = coordonnee[path[i + 1]]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=1,tags="path") 
        

genererVilles = tk.Button(root, text="Generer les villes", command=G_Villes)
genererVilles.pack()
# Création du bouton "Go"
go_button = tk.Button(root, text="Go", command=go)
go_button.pack()

def stop():
    # Fonction pour arrêter l'algorithme génétique en cours d'exécution
    global running
    running = False

# Création du bouton "Stop"
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side="top")


# Création du canevas pour dessiner les points
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Création de l'étiquette pour afficher le nombre de points
label1 = tk.Label(root, text="Nombre de points: 0")
label1.pack(side="bottom")

label2= tk.Label(root, text="Nombre de boucle: 0")
label2.pack(side="bottom")

# Lancement de la boucle principale
root.mainloop()



