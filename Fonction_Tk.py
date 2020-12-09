# Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
from Classe_jeu_du_pendu import mot_Aleatoire, jeu_du_pendu

## Fonctions permettant de faire fonctionner la fonction principale

def lettre_choisi(lettre,donnee):
    """ Fonction qui fait que la lettre donnée par l'utilisateur est prise en compte """
    if len(lettre) == 1: 
        donnee.liste_lettre.append(lettre)
        verif_lettre(donnee)
    

def verif_lettre(donnee):
    """ Fonction qui vérifie si la lettre choisi par l'utilisateur est dans le mot """
    donnee.mot_affiche = ""
    donnee.Chance = 8
    for lettre in donnee.mot_hasard :
        if lettre in donnee.liste_lettre : 
            donnee.mot_affiche += " " + lettre
        else :
            donnee.mot_affiche += " " + "_"
    for lettre in donnee.liste_lettre :
        if lettre not in donnee.mot_hasard :
            donnee.Chance -= 1
    mot_evolution(donnee) # Mise a jour du mot découvert par le joueur
    image_pendu_evolution(donnee) # Mise à jour de l'image
    Nbchance(donnee) # Mise à jour du nombre de chances restantes au joueur

def mot_evolution(donnee):
    """ Fonction qui met à jour le mot en fonction des lettres données par le joueur """
    # Création d'un widget Label (pout afficher le mot en cours de recherche)
    Motencourderech = Label(donnee.Mafenetre, text = donnee.mot_affiche, bg='grey',fg='red')
    Motencourderech.place(x=100, y=200, width=200, height=20)

def image_pendu_evolution(donnee):
    """ Fonction permettant d'afficher le pendu au fil du jeu"""
    Largeur = 300
    Hauteur = 300
    image_pendu = Canvas(donnee.Mafenetre) 
    image_pendu.create_image(0,0, anchor = 'nw', image = donnee.liste_image[donnee.Chance-1])
    image_pendu.place(x=800, y=100, width=Largeur, height=Hauteur)

def Nbchance(donnee):
    Nbchance = Label(donnee.Mafenetre, text='Il vous reste ' + str(donnee.Chance) +  ' chances', bg='grey',fg='red', font=100)
    Nbchance.place(x=400, y=200, width=200, height=20)


## Fonction du jeu du pendu

def principale():
    """Fonction principale du jeu avec l'interface graphique"""

    # Création de la fenêtre principale et initialisation des variables stockées dans le fichier Classe_jeu_du_pendu

    Mafenetre = Tk()
    Mafenetre.title('Jeu du pendu')
    Mafenetre.geometry('1200x700')

    donnee = jeu_du_pendu(Mafenetre)
    verif_lettre(donnee)

    # Création d'une phrase de bienvenue

    labelBienvenue = Label(Mafenetre, text = "Bienvenue dans le jeu du pendu",fg='red', bg= 'grey',)
    labelBienvenue.place(x=600, y=100, width=200, height=200)

    # Création d'un widget Menu

    menubar = Menu(Mafenetre)
    menuoption = Menu(menubar,tearoff =0)
    menuoption.add_command(label="Recommencer une partie", command = principale) # Boutton pour recommencer une partie
    menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy) # Boutton pour quitter 
    menubar.add_cascade(label="Option", menu = menuoption)

    # Affichage du menu
    
    Mafenetre.config(menu = menubar)

    # Fond 

    CanvaFond = Canvas(Mafenetre, bg='grey')
    CanvaFond.place(x=0, y=0, width=1200, height=700)

    
    # Création d'un widget Label (texte 'Tapez une lettre')

    Lettre = Label(Mafenetre, text='Tapez une lettre',bg='grey', fg='red')
    Lettre.place(x=20, y=330, width=100, height=50)

    # Création d'un widget Entry (pour saisir une lettre)

    lettrechoiz = StringVar()
    Champ = Entry(Mafenetre, textvariable = lettrechoiz, bg='white', fg='black')
    Champ.focus_set()
    Champ.place(x=130, y=350, width=100, height=20)

    # Création d'un widget Button (boutton pour proposer une lettre)

    buttonProposer = Button (Mafenetre, text="Proposer", fg ='red', bg='grey',relief='groove',command = lambda: lettre_choisi(lettrechoiz.get(), donnee)) 
    buttonProposer.place(x=250, y=350, width=100, height=20)

    mot_evolution(donnee)

    
   
    Nbchance(donnee) # Création d'un widget Label (pour afficher le nombre de chances restantes en fonction des lettres données par le joueur)

    image_pendu_evolution(donnee) #Affiche le pendu a droite en fonction du nomr d'erreur

    # Création d'un widget Button (boutton quitter)
    buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='red',relief='groove', command = Mafenetre.destroy)
    buttonQuitt.place(x=20, y=600, width=100, height=50)

    Mafenetre.mainloop()
