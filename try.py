# Initialiser la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid():
    print("    A   B   C")
    for i in range(3):
        print(f" {i+1} | {grid[i][0]} | {grid[i][1]} | {grid[i][2]} |")
        if i < 2:
            print("  -------------")

# Fonction pour vérifier la victoire
def verif_victoire(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            return True
    if plateau[0][0] == plateau[1][1] == plateau[1][1] == plateau[2][2] != " ":
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return True
    return False

# Fonction principale pour jouer
def jouer():
    print("Bienvenue dans le jeu de morpion !")
    joueur = "X"
    tour = 1
    victoire = True 

    while victoire:
        print_grid()  # Affiche la grille à chaque tour
        print(f"Tour {tour} : c'est au joueur {joueur}")

        # Demande à l'utilisateur de choisir la ligne
        try:
            ligne = int(input("Entrez le numéro de la ligne (1-3) : "))
            if ligne < 1 or ligne > 3:
                raise ValueError
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro de ligne entre 1 et 3.")
            continue

        # Demande à l'utilisateur de choisir la colonne
        colonne = input("Entrez la lettre de la colonne (A-C) : ").strip().upper()
        if colonne not in ["A", "B", "C"]:
            print("Entrée invalide. Veuillez entrer une lettre entre A et C.")
            continue

        # Conversion de la colonne en index
        colonne_index = {"A": 0, "B": 1, "C": 2}[colonne]

        # Vérifie si la case est vide
        if grid[ligne - 1][colonne_index] == " ":
            grid[ligne - 1][colonne_index] = joueur
            if verif_victoire(grid):
                print_grid()
                print(f"Félicitations, joueur {joueur} a gagné !")
                victoire = False
            elif tour == 9:
                print("Match nul !")
                break
            # Change de joueur pour le prochain tour
            joueur = "O" if joueur == "X" else "X"
            tour += 1
        else:
            print("Case déjà occupée, veuillez réessayer.")

        # Demande si le joueur veut rejouer après la fin du jeu
    if input("Voulez-vous rejouer ? (o/n) : ").lower() == "n":
        print("Merci d'avoir joué !")

jouer()