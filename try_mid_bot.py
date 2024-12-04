import random

# Affichage du terrain de jeu avec des colonnes A, B, C et des lignes 1, 2, 3
def afficher_grille(grille):
    print("\n   A   B   C")
    print("  -----------")
    for i in range(3):
        print(f"{i+1} | {grille[i*3]} | {grille[i*3+1]} | {grille[i*3+2]} |")
    print("  -----------\n")

# Vérification de la victoire
def verifier_victoire(grille, symbole):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    for combinaison in combinaisons_gagnantes:
        if grille[combinaison[0]] == grille[combinaison[1]] == grille[combinaison[2]] == symbole:
            return True
    return False

# Fonction pour vérifier si la grille est pleine
def grille_pleine(grille):
    return " " not in grille

# Fonction de placement du joueur
def jouer_coup(grille, index, symbole):
    if grille[index] == " ":
        grille[index] = symbole
        return True
    return False


# Heuristique simple pour le bot moyen (prioriser les cases gagnantes)
def bot_moyen(grille, symbole_bot, symbole_joueur):
    for i in range(9):
        copie_grille = grille[:]
        if copie_grille[i] == " ":
            copie_grille[i] = symbole_bot
            if verifier_victoire(copie_grille, symbole_bot):
                return i
    for i in range(9):
        copie_grille = grille[:]
        if copie_grille[i] == " ":
            copie_grille[i] = symbole_joueur
            if verifier_victoire(copie_grille, symbole_joueur):
                return i
    return bot_facile(grille)
