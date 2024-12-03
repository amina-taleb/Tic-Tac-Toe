
grid = [[" " for _ in range(3)] for _ in range(3)]


def print_grid():
    print("   A   B   C")
    for i in range(3):
        print(f" {i+1} {grid[i][0]} | {grid[i][1]} | {grid[i][2]} ")
        if i < 2:
         print("  ---+---+---")


print_grid()


#generer un bot en mode debutant
           
def bot_game():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = "O"  # Le bot joue avec "O"
                return