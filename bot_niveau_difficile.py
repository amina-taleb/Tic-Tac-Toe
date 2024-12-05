# Joueur = X se met sur la case du milieu 
# IA = O
# On va décrire un seul scénario
joueur_humain = 'X'
joueur_IA = 'O'

def vectoire_IA(grille, placement_humain, placement_IA, coup_humain) : #grille = coordonnées grille 

    for coup_humain in range (1, 8, 2) :

        if grille[1][1] == joueur_humain :  # premier coup du joueur (X au milieu) step 1
            placement_IA = grille[0][0]
            affiche_grille(grille)
        

        if placement_humain == grille[0][2] : # 2 eme coup du joueur (X en haut à droite) step 3
            placement_IA = grille[2][0]
            affiche_grille(grille)


        if placement_humain == grille[1][0] : # 3 eme coup du joueur (X au milieu gauche) step 5
            placement_IA = grille[1][2]
            affiche_grille(grille)

        if placement_humain == grille[2][1] : # 4 eme coup du joueur(X en bas au milieu) step 7
            placement_IA = grille[0][1]
            affiche_grille(grille)

    
        
