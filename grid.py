 #Initialiser la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid():
    print("-------------")
    for i in range(3):
        print(f"| {grid[i][0]} | {grid[i][1]} | {grid[i][2]} |")
        print("-------------")

# Exemple d'utilisation
print_grid()