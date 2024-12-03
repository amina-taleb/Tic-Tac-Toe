def afficher_plateau(plateau): #def print_grid(grid)
    print("   A   B   C")
    print ("1  " +plateau[0][0]+ " | " + plateau[0][1] + " | " + plateau[0][2])
    print (" ----+---+---")
    print ("2  "+plateau[1][0]+ " | " + plateau[1][1] + " | " + plateau[1][2])
    print (" ----+---+---")
    print ("3  "+plateau[2][0]+ " | " + plateau[2][1] + " | " + plateau[2][2])

def verif_victoire(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau [i][2] != " ":
            return True 
        if plateau[0][i] == plateau[1][i] == plateau [2][i] != " ":
            return True
    if plateau[0][0] == plateau [1][1] == plateau[2][2] != " ":    
        return True
    if plateau[0][2] == plateau [1][1] == plateau[2][0] != " ":
        return True
    return False 

def jouer():
    print("Bienvenue dans le jeu de morpion !")
    while True:
       plateau =[[" ", " ", " " ], [" ", " ", " " ], [" ", " ", " " ]] 
       joueur = "X"
       tour=1
       while True:
           afficher_plateau(plateau)
           print(f"Tour{tour} : c'est au joueur {joueur} ")
           
           try:
                ligne = int(input("Entrez le numéro de la ligne (1-3) : ")).strip()
                if ligne < 1 or ligne > 3:
                    raise ValueError
           except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro de ligne entre 1 et 3.")
                continue
           
           
                # Demande la colonne
           colonne = input("Entrez la lettre de la colonne (A-C) : ").strip().upper()
           if colonne not in ["A", "B", "C"]:
                print("Entrée invalide. Veuillez entrer une lettre entre A et C.")
                continue
           
                # Conversion de la colonne en index
           colonne_index = {"A": 0, "B": 1, "C": 2}[colonne]
           
           
           if plateau[ligne-1][colonne_index] ==  " ":
              plateau[ligne-1][colonne_index] = joueur
              if verif_victoire(plateau):
                  print(f"Félicitations, joueur {joueur} a gagné")
                  break
              elif tour == 9 : 
                  print("Match nul !")
                  break
              joueur = "O" if joueur == "X" else "X"
              tour += 1
           else:
               print("Case déjà occupée, veuillez réessyer.")
       if input("Voulez-vous rejouer ? (o/n)") == "n":
            break

jouer()
  