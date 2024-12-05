# Début du jeu : introduction 
def ask_name():
    while True:
        name = input("\nWhat is your name ? ").strip()  # Utilisation de strip() pour enlever les espaces inutiles
        if not name:  # Si le nom est vide ou ne contient que des espaces
            print("\nPlease enter a valid name.")
        else:
            print(f"\nWelcome {name} !")
            return name  # Retourner le nom une fois qu'il est valide

def show_rules():
    while True:
        show_rules = input("\nWould you like to see the game rules (yes/no) ? ").lower().strip()
        if show_rules == "yes":
            print("\nGame rules:\n- The goal is to align three identical symbols (X or O) horizontally, vertically, or diagonally.\n- The game is played on a 3x3 grid.\n you will play with a bot named Pixi ! ")
        elif show_rules == "no":
            print("\nOkey, let's continue")
        else:
            print("\nPlease enter only 'yes' or 'no' ")
            continue  # Redemander si l'entrée est invalide
        break



def choose_symbol():
    while True:
        player_symbol = input("\nChoose your symbol (X or O): ").upper().strip()
        if player_symbol == "X":
            bot_symbol = "O"
            print(f"\nGood, you are {player_symbol} and Pixi the bot is {bot_symbol}.")
            return player_symbol, bot_symbol
        elif player_symbol == "O":
            bot_symbol = "X"
            print(f"\nGood, you are {player_symbol} and Pixi the bot is {bot_symbol}.")
            return player_symbol, bot_symbol
        else:
            print("\nPlease enter the symbols 'O' or 'X'.")


def choose_starter(player_symbol, bot_symbol):
    while True:
        start = input("\nDo you want to start playing or let the bot play ? (play/bot) ").lower().strip()
        if start == "play":
            print("\nYou will start the game !")
            return player_symbol  # The human player starts
        elif start == "bot":
            print("\nThe bot Pixi will start the game !")
            return bot_symbol  # The bot starts
        else:
            print("\nPlease enter only 'play' or 'bot'.")

def choose_difficulty():
    while True:
        difficulty = input("\nChoose the difficulty level (easy/medium/hard): ").lower().strip()
        if difficulty in ["easy", "medium", "hard"]:
            print(f"\nYou chose {difficulty} difficulty. Good luck!")
            return difficulty
        else:
            print("\nPlease choose a valid difficulty level: easy, medium, or hard.")
           
def start_game():
    print("\nWelcome to the Tic-Tac-Toe game !")
    name = ask_name()  # Ask and validate the player's name
    show_rules()  # Show the rules if necessary
    player_symbol, bot_symbol = choose_symbol()  # Choose the symbols
    player = choose_starter(player_symbol, bot_symbol)  # Determine who starts
    difficulty = choose_difficulty()  # Choose the difficulty level

    # Séparation visuelle et pause
    print("\n" + "-" * 30)
    input("\nThe game starts now, press Enter ! ")
    print("\n" + "-" * 30)
    return player, player_symbol, bot_symbol, name, difficulty  # Return these values to start the game


# Création de la grille vide
grid = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def print_grid(grid) :
    print("     A    B   C")
    for i in range(3):
        print(f" {i+1} | {grid[i][0]} | {grid[i][1]}  | {grid[i][2]} |")
        if i < 2:
            print("   +---+----+---+")

# Fonction pour demander une position valide
def ask_position():
    COLUMN_MAPPING = {"A": 0, "B": 1, "C": 2}  # Columns: A, B, C -> indices 0, 1, 2

    while True:
        row = input("\nEnter the row number (1-3): ").strip()
        if not (row.isdigit() and 1 <= int(row) <= 3):
            print("\nInvalid input for the row. Please enter a number between 1 and 3. ")
            continue
        column = input("\nEnter the letter corresponding to the column (A-C): ").strip().upper()
        if column not in COLUMN_MAPPING:
            print("\nInvalid input for the column. Please enter a letter between A and C.")
            continue

        return int(row) - 1, COLUMN_MAPPING[column] # Conversion et retour de la position

# Fonction pour vérifier la victoire
def check_victory(grid):
    # Vérifie lignes et colonnes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " " or grid[0][i] == grid[1][i] == grid[2][i] != " ":
            return True
    # Vérifie diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != " " or grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return True
    return False

# Fonction du bot qui joue à la première case vide
def easy_bot(bot_symbol, grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = bot_symbol  # The bot plays with the symbol that the player didn't choose
                return
            
def medium_bot(bot_symbol, grid, player_symbol):
    # Check if the bot can win
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = bot_symbol
                if check_victory(grid):
                    return  # Win immediately
                grid[i][j] = " "  # Undo temporary move

    # Vérifie si le bot doit bloquer l'adversaire
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = player_symbol
                if check_victory(grid):
                    grid[i][j] = bot_symbol  # Block the human player
                    return
                grid[i][j] = " "  # Annuler le coup temporaire

    # Prendre le centre si disponible
    if grid[1][1] == " ":
        grid[1][1] = bot_symbol
        return

    # Prendre un coin si disponible
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if grid[i][j] == " ":
            grid[i][j] = bot_symbol
            return

    # Choisir une case vide (en dernier recours)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = bot_symbol
                return

def ask_replay():
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if replay == "yes":
            return True  # Replay
        elif replay == "no":
            print("\nThanks for playing! See you soon.")
            return False  # Don't replay
        else:
            print("\nInvalid response, please enter 'yes' or 'no'.")


# Fonction principale pour jouer au jeu niveau facile 
def play_easy(player, player_symbol, bot_symbol, grid, name):
    turn = 1
    current_player = player_symbol
    if player != player_symbol:  # If it's the bot's turn first
        current_player = bot_symbol  # Le bot commence immédiateme

    while turn <= 9:
        print_grid(grid)
        if current_player == player_symbol:  # The human player plays
            print(f"\nIt's your turn.({current_player})")
            row, column = ask_position()

            # Check if the spot is already taken
            if grid[row][column] == " ":
                grid[row][column] = player_symbol
                if check_victory(grid):
                    print_grid(grid)
                    print(f"\nCongratulations! you won ({current_player}).")
                    break
                # Switch to the next player
                current_player = bot_symbol
                turn += 1
            else:
                print("\nSpot already taken, try again.")
        else:  # The bot plays
            print(f"\nIt's Pixi's turn ({current_player}).")
            easy_bot(bot_symbol, grid)  # The bot plays
            if check_victory(grid):
                print_grid(grid)
                print(f"\nOh no! Pixi the bot won ({current_player}).")
                break
            current_player = player_symbol  # Switch to the human player
            turn += 1

    if turn > 9:
        print_grid(grid)
        print("\nIt's a tie!")

    # Ask if the player wants to replay
    if ask_replay():
        # Reset the grid for the new game
        grid = [[" " for _ in range(3)] for _ in range(3)]
        # Start the game again with the same parameters
        print("\nThe game restarts now, press Enter!")
        input()  # Press Enter to continue the game
        play_easy(player, player_symbol, bot_symbol, grid, name)

# Fonction principale pour jouer au jeu niveau moyen 
def play_medium(player, player_symbol, bot_symbol, grid, name):
    turn = 1
    current_player = player_symbol
    if player != player_symbol:  # If it's the bot's turn first
        current_player = bot_symbol  # Le bot commence immédiatement

    while turn <= 9:
        print_grid(grid)
        if current_player == player_symbol:  # The human player plays
            print(f"\nIt's your turn ({current_player}).")
            row, column = ask_position()

            # Check if the spot is already taken
            if grid[row][column] == " ":
                grid[row][column] = player_symbol
                if check_victory(grid):
                    print_grid(grid)
                    print(f"\nCongratulations! You won.")
                    break
                # Switch to the next player
                current_player = bot_symbol
                turn += 1
            else:
                print("\nSpot already taken, try again.")
        else:  # The bot plays
            print(f"\nIt's Pixi's turn ({current_player}).")
            medium_bot(bot_symbol, grid, player_symbol)  # The bot plays
            if check_victory(grid):
                print_grid(grid)
                print(f"\nOh no! Pixi won ({current_player}).")
                break
            current_player = player_symbol  # Switch to the human player
            turn += 1

    if turn > 9:
        print_grid(grid)
        print("\nIt's a tie!")


    # Ask if the player wants to replay
    if ask_replay():
        # Reset the grid for the new game
        grid = [[" " for _ in range(3)] for _ in range(3)]
        # Start the game again with the same parameters
        print("\nThe game restarts now, press Enter!")
        input()  # Press Enter to continue the game
        play_medium(player, player_symbol, bot_symbol, grid, name)

def play_hard(player, player_symbol, bot_symbol, grid, name):
    print("\nThe hard game mode is under development.")


# Main game loop: Starts the game depending on difficulty chosen
def main():
    player, player_symbol, bot_symbol, name, difficulty = start_game()

    if difficulty == "easy":
        play_easy(player, player_symbol, bot_symbol, grid, name)
    elif difficulty == "medium":
        play_medium(player, player_symbol, bot_symbol, grid, name)
    elif difficulty == "hard":
        play_hard(player, player_symbol, bot_symbol, grid, name)

# Start the game
if __name__ == "__main__":
    main()
