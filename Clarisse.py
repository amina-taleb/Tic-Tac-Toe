# Morane
# def initialiser_grille():
#     return [[" " for _ in range(3)] for _ in range(3)]

# def afficher_grille(grille):
#     for ligne in grille:
#         print("|".join(ligne))
#     print("-" * 5)

# def grille_pleine(grille):
#     for ligne in grille:
#         if " " in ligne:
#             return False
#     return True


# Clarisse
def demander_coup(joueur, grille):
    while True:
        try:
            print(f"Joueur {joueur}, entrez votre coup (ligne colonne) : ")
            ligne, colonne = map(int, input().split())
            
            if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
                print("Coordonnées hors de la grille. Réessayez.")
                return
            
            elif grille[ligne][colonne] != " ":
                print("Case déjà occupée. Réessayez.")
                return
            
            return ligne, colonne
        except ValueError:
            print("Entrée invalide. Entrez deux nombres entiers séparés par un espace.")

def jouer_coup(joueur, ligne, colonne, grille):
    symbole = "X" if joueur == 1 else "O"
    grille[ligne][colonne] = symbole


# Amina
# def verifier_vainqueur(grille):
#     # Vérifie les lignes et les colonnes
#     for i in range(3):
#         if grille[i][0] == grille[i][1] == grille[i][2] != " ":
#             return grille[i][0]
#         if grille[0][i] == grille[1][i] == grille[2][i] != " ":
#             return grille[0][i]
    
#     # Vérifie les diagonales
#     if grille[0][0] == grille[1][1] == grille[2][2] != " ":
#         return grille[0][0]
#     if grille[0][2] == grille[1][1] == grille[2][0] != " ":
#         return grille[0][2]
    
#     return None

# def jouer():
#     grille = initialiser_grille()
#     afficher_grille(grille)
    
#     for tour in range(9):
#         joueur = 1 if tour % 2 == 0 else 2
#         ligne, colonne = demander_coup(joueur, grille)
#         jouer_coup(joueur, ligne, colonne, grille)
        
#         afficher_grille(grille)
        
#         vainqueur = verifier_vainqueur(grille)
#         if vainqueur:
#             print(f"Le joueur {1 if vainqueur == 'X' else 2} a gagné !")
#             return
        
#         if grille_pleine(grille):
#             print("Match nul !")
#             return

#     print("Match nul !")  # Sécurité en cas d'erreur inattendue

# Lance le jeu
# jouer()
