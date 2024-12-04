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

# Choix du bot en mode facile (choix aléatoire)
def bot_facile(grille):
    index = random.choice([i for i in range(9) if grille[i] == " "])
    return index

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

# Minimax pour le bot difficile
def minimax(grille, profondeur, maximizing_player, symbole_bot, symbole_joueur):
    if verifier_victoire(grille, symbole_bot):
        return 1
    elif verifier_victoire(grille, symbole_joueur):
        return -1
    elif grille_pleine(grille):
        return 0

    if maximizing_player:
        meilleur_score = -float('inf')
        meilleur_coup = None
        for i in range(9):
            if grille[i] == " ":
                grille[i] = symbole_bot
                score = minimax(grille, profondeur + 1, False, symbole_bot, symbole_joueur)
                grille[i] = " "
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = i
        return meilleur_score if profondeur != 0 else meilleur_coup
    else:
        meilleur_score = float('inf')
        meilleur_coup = None
        for i in range(9):
            if grille[i] == " ":
                grille[i] = symbole_joueur
                score = minimax(grille, profondeur + 1, True, symbole_bot, symbole_joueur)
                grille[i] = " "
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = i
        return meilleur_score if profondeur != 0 else meilleur_coup

# Fonction pour convertir la saisie de l'utilisateur (A1, B2, etc.) en index de la grille
def conversion_pos(position):
    colonnes = {'A': 0, 'B': 1, 'C': 2}
    lignes = {'1': 0, '2': 1, '3': 2}
    return lignes[position[1]] * 3 + colonnes[position[0]]

# Jeu principal
def jouer():
    print("Bienvenue au jeu du Morpion!")
    nom = input("Quel est ton nom ? ")
    print(f"Bienvenue {nom} !")
    afficher_regles = input("Souhaites-tu voir les règles du jeu (oui/non) ? ").lower()
    if afficher_regles == "oui":
        print("\nRègles du jeu :\n- Le but est d'aligner trois symboles identiques (X ou O) horizontalement, verticalement ou en diagonale.\n- Le jeu se joue sur une grille de 3x3 avec des colonnes A, B, C et des lignes 1, 2, 3.")
    input("Appuie sur Enter pour commencer le jeu.")

    commencer = input("Veux-tu commencer à jouer ou laisser le bot jouer ? (jouer/bot) ").lower()
    if commencer != "jouer":
        print("Merci d'avoir joué !")
        return

    symbole_joueur = input("Choisis ton symbole (X ou O) : ").upper()
    symbole_bot = "O" if symbole_joueur == "X" else "X"

    niveau = input("Choisis le niveau de difficulté (facile/moyen/difficile) : ").lower()

    while True:
        grille = [" " for _ in range(9)]
        tour_joueur = True
        while True:
            afficher_grille(grille)
            if tour_joueur:
                position = input(f"Choisis une case (ex : A1, B2, C3) pour {symbole_joueur}: ").upper()
                if len(position) == 2 and position[0] in "ABC" and position[1] in "123":
                    coup = conversion_pos(position)
                    if jouer_coup(grille, coup, symbole_joueur):
                        if verifier_victoire(grille, symbole_joueur):
                            afficher_grille(grille)
                            print(f"{nom} a gagné !")
                            break
                    else:
                        print("Case déjà occupée. Essaie encore.")
                else:
                    print("Position invalide, essaie encore.")
            else:
                if niveau == "facile":
                    coup = bot_facile(grille)
                elif niveau == "moyen":
                    coup = bot_moyen(grille, symbole_bot, symbole_joueur)
                else:
                    coup = minimax(grille, 0, True, symbole_bot, symbole_joueur)
                jouer_coup(grille, coup, symbole_bot)
                print(f"Le bot a joué en {['A', 'B', 'C'][coup%3]}{(coup//3)+1}")
                if verifier_victoire(grille, symbole_bot):
                    afficher_grille(grille)
                    print("Le bot a gagné !")
                    break

            if grille_pleine(grille):
                afficher_grille(grille)
                print("Match nul!")
                break

            tour_joueur = not tour_joueur

        rejouer = input("Veux-tu rejouer (oui/non) ? ").lower()
        if rejouer != "oui":
            break

# Exécution du jeu
if __name__ == "__main__":
    jouer()
