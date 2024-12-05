
def bot_game():
    # Vérifie si le bot peut gagner
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = "O"
                if verif_victoire("O"):
                    return  # Gagner immédiatement
                grid[i][j] = " "  # Annuler le coup temporaire

    # Vérifie si le bot doit bloquer l'adversaire
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = "X"
                if verif_victoire("X"):
                    grid[i][j] = "O"  # Bloquer le joueur humain
                    return
                grid[i][j] = " "  # Annuler le coup temporaire

    # Prendre le centre si disponible
    if grid[1][1] == " ":
        grid[1][1] = "O"
        return

    # Prendre un coin si disponible
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if grid[i][j] == " ":
            grid[i][j] = "O"
            return

    # Choisir une case vide (en dernier recours)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = "O"
                return