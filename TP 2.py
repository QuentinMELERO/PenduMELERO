# Header

""" 
Programme pour jeu du Pendu
Réalisé par Adrien Corsetti et Quentin Melero le 01/12/2020
Fini

"""

# Importation des bibliothèques nécessaires 

from Fonction import jeu_du_pendu, mot_aleatoire


# Fonction principale

score_max = 0 # Initialisation du score maximum de l'utilisateur qui n'a pas encore joué

mon_fichier = open("mots.txt",'r') # On ouvre le fichier mots.txt
mots_pendu = mon_fichier.readlines() # Liste des mots proposés au joueur
mon_fichier.close() # On ferme le fichier mots.txt

jeu_du_pendu(mots_pendu,score_max) # Une partie commence


