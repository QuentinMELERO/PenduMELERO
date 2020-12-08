# Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
from Fonction import evolution_du_mot_deviner, jeu_du_pendu, mot_aleatoire

## Fonctions pour les commandes

def scoremax():
    scoreMax = max(score_max,chance)
    return scoreMax

def recomjeu():
    return

def soumettrelettre():
    global mot_aleatoire, lettrechoiz, Champ,Motencourderech,Nbchance , buttonProposer, scoremax
    if len(Champ.get()) != 1 or not Champ.get().isalpha() or Champ.get().lower() in lettrechoiz:
        Champ.set("")  # Reset le input
        return 
    lettrechoiz += Champ.get().lower()
    Champ.set("")
    if Motencourderech.get() == getWordFromSerialLetters(mot_aleatoire, lettrechoiz): # Fonction donné par le prof que je ne comprends pas 
        Nbchance.set(int(Nbchance.get()) - 1)  # Enleve une chance à l'utilisateur qui en dispose de 8
    if int(Nbchance.get()) == 0:  # Case si il l'utilisateur n'a plus de vie
        Motencourderech.set()
        highScore = 0
        Nbchance.set("Tu as perdu")
        Canevas.delete("all")
        Canevas.create_image(0, 0, anchor="nw", image=photo1)
        buttonProposer.config(text="Commencer une nouvelle partie", command=recomjeu)
        return
    Motencourderech.set(getWordFromSerialLetters(Motencourderech, lettrechoiz)) # Fonction donné par le prof que je ne comprends pas
    if getWordFromSerialLetters(Motencourderech, lettrechoiz) == mot_aleatoire:  # Case si le mot est trouvé
        Nbchance.set("Gagné, bravo champion!")
        highScore += 1
    if Nouveauscore() < highScore:
        scoremax(highScore)
        buttonProposer.config(text="Commencer une nouvelle partie", command=recomjeu)


## Interface graphique

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Jeu du pendu')
Mafenetre.geometry('1200x700')

# Image du pendu
photo1 = PhotoImage(file='bonhomme1.gif')
photo2 = PhotoImage(file='bonhomme2.gif')
photo3 = PhotoImage(file='bonhomme3.gif')
photo4 = PhotoImage(file='bonhomme4.gif')
photo5 = PhotoImage(file='bonhomme5.gif')
photo6 = PhotoImage(file='bonhomme6.gif')
photo7 = PhotoImage(file='bonhomme7.gif')
photo8 = PhotoImage(file='bonhomme8.gif')

# Création d'une phrase de bienvenue
labelBienvenue = Label (Mafenetre, text = "Bienvenue dans le jeu du pendu", fg = 'black',font=(100))
labelBienvenue.pack()

# Création d'un widget Menu
menubar = Menu(Mafenetre)
menuoption = Menu(menubar,tearoff =0)
menuoption.add_command(label="Recommencer une partie", command = recomjeu)
menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy)
menubar.add_cascade(label="Option", menu = menuoption)

# Affichage du menu
Mafenetre.config(menu = menubar)

# Création d'un widget Label (texte 'Tapez une lettre')
Lettre = Label(Mafenetre, text='Tapez une lettre')
Lettre.pack(side='left',padx=5, pady=50)

# Création d'un widget Entry (pour saisir une lettre)
lettrechoiz = StringVar()
Champ = Entry(Mafenetre, textvariable= lettrechoiz, bg='white', fg='black')
Champ.focus_set()
Champ.pack(side='left',padx=5, pady=50)

# Création d'un widget Button (boutton pour proposer une lettre)
buttonProposer = Button (Mafenetre, text="Proposer", fg ='black', bg='white',relief='groove',command = soumettrelettre)
buttonProposer.pack(side='left', padx=5, pady=50)

# Création d'un widget Label (pout afficher le mot en cours de recherche)
Motencourderech = Label(Mafenetre, text='')
Motencourderech.pack(side='left',padx=5)

# Création d'un widget Label (pour afficher le nombre de chances restantes)
Nbchance = Label(Mafenetre, text='Il vous reste chances' )
Nbchance.pack(side='left',padx=5)

# Création d'un widget Canvas
Largeur = 300
Hauteur = 300
Canevas = Canvas(Mafenetre, width = Largeur, height = Hauteur)
item = Canevas.create_image(0,0,anchor='nw',image=photo8)
Canevas.pack()

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='black', bg='white',relief='groove', command = Mafenetre.destroy)
buttonQuitt.pack(side='left',padx=5, pady=50)

Mafenetre.mainloop()

