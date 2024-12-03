 #Initialiser la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid():
    print("    A   B   C")
    for i in range(3):
        print(f" {i+1}| {grid[i][0]} | {grid[i][1]} | {grid[i][2]} |")
        if i < 2:
         print("  -------------")

# Exemple d'utilisation
print_grid()