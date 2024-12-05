#A faire: améliorer les instructions du jeu

# Début du jeu : introduction 
def demander_nom():
    while True:
        nom = input("\nQuel est ton nom ? ").strip()  # Utilisation de strip() pour enlever les espaces inutiles
        if not nom:  # Si le nom est vide ou ne contient que des espaces
            print("\nMerci de rentrer un nom valide.")
        else:
            print(f"\nBienvenue {nom} !")
            return nom  # Retourner le nom une fois qu'il est valide

def afficher_regles():
    while True:
        afficher_regles = input("\nSouhaites-tu voir les règles du jeu (oui/non) ? ").lower().strip()
        if afficher_regles == "oui":
            print("\nRègles du jeu :\n- Le but est d'aligner trois symboles identiques (X ou O) horizontalement, verticalement ou en diagonale.\n- Le jeu se joue sur une grille de 3x3.")
        elif afficher_regles == "non":
            print("\nOk, dans ce cas, continuons.")
        else:
            print("\nJe n'ai pas bien compris, merci de rentrer 'oui' ou 'non'.")
            continue  # Redemander si l'entrée est invalide
        break


def choisir_symbole():
    while True:
        symbole_joueur = input("\nChoisis ton symbole (X ou O) : ").upper().strip()
        if symbole_joueur == "X":
            symbole_bot = "O"
            print(f"\nGood, tu es le {symbole_joueur} et le bot est le {symbole_bot}.")
            return symbole_joueur, symbole_bot
        elif symbole_joueur == "O":
            symbole_bot = "X"
            print(f"\nGood, tu es le {symbole_joueur} et le bot est le {symbole_bot}.")
            return symbole_joueur, symbole_bot
        else:
            print("\nMerci de rentrer les symboles 'O' ou 'X'.")


def choisir_commenceur(symbole_joueur, symbole_bot):
    while True:
        commencer = input("\nVeux-tu commencer à jouer ou laisser le bot jouer ? (jouer/bot) ").lower().strip()
        if commencer == "jouer":
            print("\nC'est donc toi qui commenceras le jeu !")
            return symbole_joueur  # Le joueur humain commence
        elif commencer == "bot":
            print("\nC'est donc le bot qui commencera le jeu !")
            return symbole_bot  # Le bot commence
        else:
            print("\nMerci de rentrer uniquement les mots 'jouer' ou 'bot'.")

def choisir_niveau():
    while True:
        niveau = input("\nChoisis le niveau de difficulté (facile/moyen/difficile) : ").lower().strip()
        if niveau in ["facile", "moyen", "difficile"]:
            print(f"\nTu as choisi le niveau {niveau}. Bonne chance !")
            return niveau
        else:
            print("\nMerci de choisir un niveau valide : facile, moyen ou difficile.")
           
def demarrer_jeu():
    print("\nBienvenue au jeu du Morpion!")
    nom = demander_nom()  # Demander et valider le nom du joueur
    afficher_regles()  # Afficher les règles si nécessaire
    symbole_joueur, symbole_bot = choisir_symbole()  # Choisir les symboles
    joueur = choisir_commenceur(symbole_joueur, symbole_bot)  # Déterminer qui commence
    niveau = choisir_niveau()  # Choisir le niveau de difficulté

    # Séparation visuelle et pause
    print("\n" + "-" * 30)
    input("\nLe jeu commence maintenant, Appuyez sur Entrée !")
    print("\n" + "-" * 30)
    return joueur, symbole_joueur, symbole_bot, nom, niveau # Retourner ces valeurs pour commencer le jeu

 
# Création de la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid(grid) -> tuple[int, int]:
    print("     A    B   C")
    for i in range(3):
        print(f" {i+1} | {grid[i][0]} | {grid[i][1]}  | {grid[i][2]} |")
        if i < 2:
            print("   +---+----+---+")

# Fonction pour demander une position valide
def demander_position():
    CORRESPONDANCE_COLONNES = {"A": 0, "B": 1, "C": 2}  # Colonnes : A, B, C -> indices 0, 1, 2

    while True:
        ligne = input("Entrez le numéro correspondant à la ligne (1-3) : ").strip()
        if not (ligne.isdigit() and 1 <= int(ligne) <= 3):
            print("Entrée invalide pour la ligne. Veuillez entrer un chiffre entre 1 et 3.")
            continue
        colonne = input("Entrez le caractère correspondant à la colonne (A-C) : ").strip().upper()
        if colonne not in CORRESPONDANCE_COLONNES:
            print("Entrée invalide pour la colonne. Veuillez entrer une lettre entre A et C.")
            continue

        return int(ligne) - 1, CORRESPONDANCE_COLONNES[colonne]  # Conversion et retour de la position

# Fonction pour vérifier la victoire
def verif_victoire(grid):
    # Vérifie lignes et colonnes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " " or grid[0][i] == grid[1][i] == grid[2][i] != " ":
            return True
    # Vérifie diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != " " or grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return True
    return False

# Fonction du bot qui joue à la première case vide
def bot_facile(symbole_bot, grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = symbole_bot  # Le bot joue avec le symbole que n'a pas choisi l'utilisateur
                return
            
def bot_moyen(symbole_bot, grid, symbole_joueur):
    # Vérifie si le bot peut gagner
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = symbole_bot
                if verif_victoire(grid):
                    return  # Gagner immédiatement
                grid[i][j] = " "  # Annuler le coup temporaire

    # Vérifie si le bot doit bloquer l'adversaire
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] =symbole_joueur
                if verif_victoire(grid):
                    grid[i][j] = symbole_bot  # Bloquer le joueur humain
                    return
                grid[i][j] = " "  # Annuler le coup temporaire

    # Prendre le centre si disponible
    if grid[1][1] == " ":
        grid[1][1] = symbole_bot
        return

    # Prendre un coin si disponible
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if grid[i][j] == " ":
            grid[i][j] = symbole_bot
            return

    # Choisir une case vide (en dernier recours)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = symbole_bot
                return

def demander_rejouer():
    while True:
        rejouer = input("Veux-tu rejouer ? (oui/non) : ").lower().strip()
        if rejouer == "oui":
            return True  # Rejouer
        elif rejouer == "non":
            print("Merci d'avoir joué ! À bientôt.")
            return False  # Ne pas rejouer
        else:
            print("Réponse invalide, merci de rentrer 'oui' ou 'non'.")

# Fonction principale pour jouer au jeu niveau facile 
def jouer_facile(joueur, symbole_joueur, symbole_bot, grid, nom ):
    tour = 1
    joueur_actuel = symbole_joueur
    if joueur != symbole_joueur:  # Si c'est le bot qui commence
        joueur_actuel = symbole_bot  # Le bot commence immédiateme

    while tour <= 9:
        print_grid(grid)
        if joueur_actuel == symbole_joueur :  # Le joueur humain joue
            print(f"C'est au tour du joueur {joueur}.")
            ligne, colonne = demander_position()

            # Vérifie si la case est déjà occupée
            if grid[ligne][colonne] == " ":
                grid[ligne][colonne] = symbole_joueur
                if verif_victoire(grid):
                    print_grid(grid)
                    print(f"Félicitations ! Le joueur {joueur} a gagné.")
                    break
                # Passe au joueur suivant
                joueur_actuel = symbole_bot
                tour += 1
            else:
                print("Case déjà occupée, essayez encore.")
        else:  # Le bot joue
            print(f"C'est au tour du joueur {joueur} (le bot).")
            bot_facile(symbole_bot, grid)  # Le bot joue
            if verif_victoire(grid):
                print_grid(grid)
                print(f"Oh mince! Le joueur {joueur} (le bot) a gagné.")
                break
            joueur_actuel = symbole_joueur  # Passe au joueur humain
            tour += 1

    if tour > 9:
        print_grid(grid)
        print("Match nul !")

        # Demander si le joueur veut rejouer
    if demander_rejouer():
        # Réinitialiser la grille pour la nouvelle partie
        grid = [[" " for _ in range(3)] for _ in range(3)]
         # Démarrer directement le jeu avec les mêmes paramètres
        print("\nLe jeu recommence maintenant, Appuyez sur Entrée !")
        input()  # Attente de l'entrée pour démarrer
        jouer_facile(joueur, symbole_joueur, symbole_bot, grid, nom)  # Recommencer le jeu

# Fonction principale pour jouer au jeu niveau moyen 
def jouer_moyen(joueur, symbole_joueur, symbole_bot, grid, nom ):
    tour = 1
    joueur_actuel =  symbole_joueur
    if joueur != symbole_joueur:  # Si c'est le bot qui commence
       joueur_actuel = symbole_bot  # Le bot commence immédiatement

    while tour <= 9:
        print_grid(grid)
        if joueur_actuel == symbole_joueur :  # Le joueur humain joue
            print(f"C'est au tour de {joueur_actuel}.")
            ligne, colonne = demander_position()

            # Vérifie si la case est déjà occupée
            if grid[ligne][colonne] == " ":
                grid[ligne][colonne] = symbole_joueur
                if verif_victoire(grid):
                    print_grid(grid)
                    print(f"Félicitations ! Le joueur {joueur_actuel} a gagné.")
                    break
                # Passe au joueur suivant
                joueur_actuel = symbole_bot
                tour += 1
            else:
                print("Case déjà occupée, essayez encore.")
        else:  # Le bot joue
            print(f"C'est au tour du joueur {joueur_actuel} (le bot).")
            bot_moyen(symbole_bot, grid, symbole_joueur)  # Le bot joue
            if verif_victoire(grid):
                print_grid(grid)
                print(f"Oh mince! Le joueur {joueur_actuel} (le bot) a gagné.")
                break
            joueur_actuel = symbole_joueur  # Passe au joueur humain
            tour += 1

    if tour > 9:
        print_grid(grid)
        print("Match nul !")

    # Demander si le joueur veut rejouer
    if demander_rejouer():
        # Réinitialiser la grille pour la nouvelle partie
        grid = [[" " for _ in range(3)] for _ in range(3)]
         # Démarrer directement le jeu avec les mêmes paramètres
        print("\nLe jeu recommence maintenant, Appuyez sur Entrée !")
        input()  # Attente de l'entrée pour démarrer
        jouer_moyen(joueur, symbole_joueur, symbole_bot, grid, nom)  # Recommencer le jeu

def jouer_difficile(joueur, symbole_joueur, symbole_bot, grid, nom):
    print("\nLe mode difficile est en cours de développement.")


# Lancer le jeu
if __name__ == "__main__":
    joueur, symbole_joueur, symbole_bot, nom, niveau = demarrer_jeu()
    if niveau == "facile":
        jouer_facile(joueur, symbole_joueur, symbole_bot, grid, nom)
    elif niveau == "moyen":
        jouer_moyen(joueur, symbole_joueur, symbole_bot, grid, nom)
    elif niveau == "difficile":
        jouer_difficile(joueur, symbole_joueur, symbole_bot, grid, nom)