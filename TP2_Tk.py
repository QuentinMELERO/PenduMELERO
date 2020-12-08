# Header

""" 
Programme pour jeu du Pendu
Réalisé par Quentin Melero le 08/12/2020
Finir les liens entre les fonctions et les commandes de l'interface graphique, programme pas fonctionnel

"""

# Importation des bibliothèques nécessaires 

from Fonction import jeu_du_pendu, mot_aleatoire


# Fonction principale

score_max = 0 # Initialisation du score maximum de l'utilisateur qui n'a pas encore joué

mon_fichier = open("mots.txt",'r') # On ouvre le fichier mots.txt
mots_pendu = mon_fichier.readlines() # Liste des mots proposés au joueur
mon_fichier.close() # On ferme le fichier mots.txt

jeu_du_pendu(mots_pendu,score_max) # Une partie commence
