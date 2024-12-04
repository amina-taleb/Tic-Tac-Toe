# Création de la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid():
    print("    A   B   C")
    for i in range(3):
        print(f" {i+1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} |")
        if i < 2:
            print("  -------------")

# Fonction pour demander une position valide
def demander_position():
    correspondance_colonnes = {"A": 0, "B": 1, "C": 2}  # Colonnes : A, B, C -> indices 0, 1, 2

    while True:
        ligne = input("Entrez le numéro correspondant à la ligne (1-3) : ").strip()
        if not (ligne.isdigit() and 1 <= int(ligne) <= 3):
            print("Entrée invalide pour la ligne. Veuillez entrer un chiffre entre 1 et 3.")
            continue

        colonne = input("Entrez le caractère correspondant à la colonne (A-C) : ").strip().upper()
        if colonne not in correspondance_colonnes:
            print("Entrée invalide pour la colonne. Veuillez entrer une lettre entre A et C.")
            continue

        return int(ligne) - 1, correspondance_colonnes[colonne]

# Fonction pour vérifier la victoire
def verif_victoire():
    # Vérifie lignes et colonnes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " " or grid[0][i] == grid[1][i] == grid[2][i] != " ":
            return True
    # Vérifie diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != " " or grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return True
    return False

# Fonction du bot qui joue à la première case vide
def bot_game():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = "O"  # Le bot joue avec "O"
                return

# Fonction principale
def jouer():
    print("Bienvenue dans le jeu de morpion !")
    joueur = "X"  # Le premier joueur commence avec "X"
    tour = 1

    while tour <= 9:
        print_grid()
        if joueur == "X":  # Le joueur humain joue
            print(f"C'est au tour du joueur {joueur}.")
            ligne, colonne = demander_position()

            # Vérifie si la case est déjà occupée
            if grid[ligne][colonne] == " ":
                grid[ligne][colonne] = joueur
                if verif_victoire():
                    print_grid()
                    print(f"Félicitations ! Le joueur {joueur} a gagné.")
                    break
                # Passe au joueur suivant
                joueur = "O" if joueur == "X" else "X"
                tour += 1
            else:
                print("Case déjà occupée, essayez encore.")
        else:  # Le bot joue
            print(f"C'est au tour du joueur {joueur} (le bot).")
            bot_game()  # Le bot joue
            if verif_victoire():
                print_grid()
                print(f"Félicitations ! Le joueur {joueur} (le bot) a gagné.")
                break
            joueur = "X"  # Passe au joueur humain
            tour += 1

    if tour > 9:
        print_grid()
        print("Match nul !")

# Démarrer le jeu
jouer()