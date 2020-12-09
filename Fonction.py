import random as rd # Importation du module random 

## Interaction avec l'utilisateur

def evolution_du_mot_deviner(liste_lettre_restante,mot_deviner,chance,lettre_essaye):
    """ Fonction qui va animer le jeu étape par étape """
    print(" Il vous reste " + str(chance) + " "+"chances") # On informe l'utilisateur de son nombre de chances restantes
    lettre_utilise="" # On informe l'utilisateur des lettres qu'il a déjà utilisées
    for i in lettre_essaye:
       lettre_utilise += i + ", "
    print(" Vous avez déjà utilisé les lettres : " +lettre_utilise)
    
    lettre_choisi = input(" Tapez une lettre : ") # On récupère la lettre saisie par le joueur
    lettre_essaye.append(lettre_choisi)         # On l'ajoute dans la liste des lettres essayées grâce à append
    
    indice_lettre_a_montrer=[] # Mise a jour de la liste des lettres restantes et du mot a deviner à chaque fois que le joueur saisie une lettre
    for k in range(len(liste_lettre_restante)):
        if liste_lettre_restante[k][0] == lettre_choisi:
            indice_lettre_a_montrer = [k] + indice_lettre_a_montrer        
    if indice_lettre_a_montrer == []:
        print("Loupé, cette lettre n'est pas dans le mot")
        chance -= 1      
    for i in indice_lettre_a_montrer:
        mot_deviner[liste_lettre_restante[i][1]] = liste_lettre_restante[i][0]
        liste_lettre_restante.pop(i)
    return liste_lettre_restante,mot_deviner,chance,lettre_essaye  

def affichage_mot(mot_deviner): # Transformation de mot_deviner en chaine de caractères
    mot = ""
    for i in mot_deviner:
        mot += i +  " "
    return mot
    
## Choisir le mot

def mot_aleatoire():
    """ Fonction qui retourne un mot aléatoire du fichier mots.txt """
    monfichier=open('mots.txt','r')
    lignes = monfichier.readlines()
    nb_al = rd.randint(0,len(lignes))
    monfichier.close()
    return (lignes[nb_al])

## La fonction qui fait marcher le jeu

def jeu_du_pendu(mots_pendu,score_max):
    """ Fonction qui va faire marcher le jeu """
    mot_choisi= mot_aleatoire() # On choisi un mot aléatoirement parmi la liste mots_pendu, en faisant appel à la fonction précédemment définie
    liste_Lettre=[] # On sépare le mot en une liste, où chaque élément représente une lettre du mot
    for lettre in mot_choisi :
        liste_Lettre.append(lettre) # On ajoute chaque lettre du mot dans la liste précédemment initialisée via la fonction append
        liste_lettre=liste_Lettre[0:len(liste_Lettre)-1] # On enlève le dernier élément de liste_Lettre qui est le saut de ligne
    mot_deviner=[liste_lettre[0]] # Création du mot secret avec les underscores
    for i in range (1,len(liste_lettre)):
        mot_deviner.append("_")
        if liste_lettre[i]==liste_lettre[0]: # On affiche la première lettre du mot et des underscores
            mot_deviner[i]=mot_deviner[0]    # (_) pour les autres lettres qui sont différentes                                                                         
    liste_lettre_restante=[] # Création de la liste des lettres restantes du mot
    for k in range(1,len(liste_lettre)):
        if ((liste_lettre[k] != liste_lettre[0])): # Liste de liste avec pour chaque sous liste le premier élement qui
            liste_lettre_restante.append([liste_lettre[k],k]) # correspond à la lettre restante et le deuxième sa position dans le mot
    chance=8 # Le joueur peut se tromper 8 fois de lettres
    lettre_essaye=[] # Au départ le joueur n'a essayé aucune lettre
    mot_deviner_afficher = affichage_mot(mot_deviner)  # Transformation de mot_deviner en chaine de caractères
    print(mot_deviner_afficher+"\n")
    while chance>0 and liste_lettre_restante != []: # Le jeu s'arrête si le joueur a utilisé toutes ses chances ou s'il a trouvé toutes les bonnes lettres.
        liste_lettre_restante,mot_deviner,chance,lettre_essaye=evolution_du_mot_deviner(liste_lettre_restante, mot_deviner,chance,lettre_essaye) # Animation du jeu étape par étape
        mot_deviner_afficher=affichage_mot(mot_deviner) # Affichage de l'avancement du mot pour l'utilisateur
        print(mot_deviner_afficher)
    if chance == 0 :
        print("Perdu, mais le plus important c'est de participer")
    else :
        print("Gagné, bravo champion")
    score_max = max(score_max,chance) # Mise a jour du score maximum
    print(" Votre meilleur score est : " + str(score_max)) # L'utilisateur voit son meilleur score
    rejouer = input(" Voulez vous rejouez ? (oui ou non) : ")  # On propose à l'utilisateur s'il souhaite rejouer
    if (rejouer == "oui"):
        jeu_du_pendu(mots_pendu,score_max) # On relance le jeu
