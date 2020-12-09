## Page pour gérer les classes et toutes les variables de mes fonctions du programme Fonction_Tk.py

from tkinter import PhotoImage
import random as rd

def mot_Aleatoire():
    """ Fonction qui retourne un mot aléatoire du fichier mots.txt """
    monfichier=open('mots.txt','r')
    lignes = monfichier.readlines()
    nb_al = rd.randint(0,len(lignes))
    monfichier.close()
    return (lignes[nb_al][0:-1])

class jeu_du_pendu:
    def __init__(self, Mafenetre):
        # Stock des données de mon jeu
        self.mot_hasard = mot_Aleatoire() 
        self.liste_lettre = [self.mot_hasard[0]]
        self.mot_affiche = ""
        self.Mafenetre = Mafenetre
        self.Chance = 8
        self.photo1 = PhotoImage(file='bonhomme1.gif')
        self.photo2 = PhotoImage(file='bonhomme2.gif')
        self.photo3 = PhotoImage(file='bonhomme3.gif')
        self.photo4 = PhotoImage(file='bonhomme4.gif')
        self.photo5 = PhotoImage(file='bonhomme5.gif')
        self.photo6 = PhotoImage(file='bonhomme6.gif')
        self.photo7 = PhotoImage(file='bonhomme7.gif')
        self.photo8 = PhotoImage(file='bonhomme8.gif')
        self.liste_image = [self.photo8,self.photo7,self.photo6,self.photo5,self.photo4,self.photo3,self.photo2,self.photo1]