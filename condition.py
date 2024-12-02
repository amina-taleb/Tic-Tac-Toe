# grid : une fonction qui correspond aux cases 

#Je vais définir une fonction pour vérifier si l'utilisateur actuel a gagné
def gagner() :
# Conditions du succès :
    for i in range (3) :
    # Si je gagne en lignes :
    #Ligne 1 : (0, 0) = (0, 1) = (0, 2) ou 
    #Ligne 2 : (1, 0) = (1, 1) = (1, 2) ou 
    #Ligne 3 : (2, 0) = (2, 1) = (2, 2) 

        if grid[i][0] == grid[i][1] == grid[i][2] :
            return True
    # Si je gagne en colonne :
    #Ligne 1 : (0, 0) = (1, 0) = (2, 0) ou 
    #Ligne 2 : (0, 1) = (1, 1) = (2, 1) ou 
    #Ligne 3 : (0, 2) = (1, 2) = (2, 2)    

        if grid[0][i] == grid[1][1] == grid[2][i] :
            return True
    
    # Si je gagne en diagonal :
    if grid[0][0] == grid[1][1] == grid[2][2] :
        return True
    
    # Si je gagne en diagonal inversé :
    if grid[0][2] == grid[1][1] == grid[2][0] :
        return True
    

#Je vais définir une fonction qui correspond à l'arrêt du jeu :
def arreter() :

    