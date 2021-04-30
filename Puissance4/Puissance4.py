import numpy as np

nb_lignes = 6
nb_colonnes = 12
<<<<<<< HEAD
compteur = 0

=======
l=0
col=0
compteur=1
>>>>>>> origin/develop
values = {0:'Vide', 1:'Bleu', 2: 'Rouge'}
theBoard = np.zeros((nb_lignes,nb_colonnes),dtype=int)


def printBoard():
    affichage = "  ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─   ─\n"
    for i in range(0, 6):
        affichage += "| "
        for j in range(0, 12):
            affichage += f"{theBoard[i][j]} | "
        affichage += "\n"
    affichage += "  ─   ─   ─   ─   ─   ─   ─   ─   ─  ─  ─  ─  ─\n"
    print(affichage)

def canPlay(colonne):
    return theBoard[0][colonne] == 0

def getLastFreeCase(colonne):
    for i in range(5,-1,-1):
        if theBoard[i][colonne] == 0:
            return i
    return -1


<<<<<<< HEAD
def heuristique(joueur):
=======
def heuristique():
>>>>>>> origin/develop
    heur = 0
    #teste toutes les possibilités en lignes
    for i in range(6):
        for j in range(9):
            if theBoard[i][j] != 1 and theBoard[i][j+1] != 1 and theBoard[i][j+2] != 1 and theBoard[i][j+3] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i][j+1] != 2 and theBoard[i][j+2] != 2 and theBoard[i][j+3] != 2:
                heur -=1


    #teste toutes les possibilités en colonnes
    for j in range(12):
        for i in range(3):
            if theBoard[i][j] != 1 and theBoard[i+1][j] != 1 and theBoard[i+2][j] != 1 and theBoard[i+3][j] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i+1][j] != 2 and theBoard[i+2][j] != 2 and theBoard[i+3][j] != 2:
                heur -=1

    #teste toutes les possibilités en diagonales montantes / et descendantes \
    for i in range(3):
        for j in range(9):
            if theBoard[i][j] != 1 and theBoard[i+1][j+1] != 1 and theBoard[i+2][j+2] != 1 and theBoard[i+3][j+3] != 1:
                heur +=1
            if theBoard[i+3][j] != 1 and theBoard[i+2][j+1] != 1 and theBoard[i+1][j+2] != 1 and theBoard[i][j+3] != 1:
                heur +=1
            if theBoard[i][j] != 2 and theBoard[i+1][j+1] != 2 and theBoard[i+2][j+2] != 2 and theBoard[i+3][j+3] != 2:
                heur -=1
            if theBoard[i+3][j] != 2 and theBoard[i+2][j+1] != 2 and theBoard[i+1][j+2] != 2 and theBoard[i][j+3] != 2:
                heur -=1
<<<<<<< HEAD

    return heur

def minmax(board,alpha,beta, profondeur, isMaximazing,ligne,colonne,joueur):
    if(profondeur == 0 or checkWinningConditions(ligne,colonne,joueur)):
=======
    return heur

def minmax(board,alpha,beta, profondeur, isMaximazing,ligne,colonne,joueur):
    global compteur
    if(profondeur == 0 or checkWinningConditions(ligne,colonne,compteur,joueur)):
>>>>>>> origin/develop
        return heuristique()
    
    if(isMaximazing):
        maxEvaluate = np.NINF
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = 2
                evaluate = minmax(theBoard,alpha,beta, profondeur-1 ,False,ligne,colonne,1)
                theBoard[ligne][colonne] = 0
                maxEvaluate = max(maxEvaluate,evaluate)
                alpha = max(alpha,evaluate)
                if beta <= alpha:
                    break
        return maxEvaluate
    else:
        minEvaluate = np.Inf
        for colonne in np.arange(0,12):
            if canPlay(colonne):
                ligne = getLastFreeCase(colonne)
                theBoard[ligne][colonne] = 1
<<<<<<< HEAD
                evaluate = minmax(theBoard,alpha,beta, profondeur-1 ,False,ligne,colonne,2)
=======
                evaluate = minmax(theBoard,alpha,beta, profondeur-1 ,True,ligne,colonne,2)
>>>>>>> origin/develop
                theBoard[ligne][colonne] = 0
                minEvaluate = min(minEvaluate,evaluate)
                beta = min(beta,evaluate)
                if beta <= alpha:
                    break            
        return minEvaluate

def turnAI():
	#AI to make its turn
    global l,col
    move = (0,0)
    bestScore = np.NINF
    for colonne in np.arange(0,12):
        if canPlay(colonne):
            ligne = getLastFreeCase(colonne)
            theBoard[ligne][colonne] = 2
<<<<<<< HEAD
            score = minmax(theBoard,np.NINF,np.Inf, 4 ,False,ligne,colonne,2)
=======
            score = minmax(theBoard,np.NINF,np.Inf, 1 ,False,ligne,colonne,1)
>>>>>>> origin/develop
            theBoard[ligne][colonne] = 0
            if score > bestScore:
                bestScore = score
                move = (ligne,colonne)
    theBoard[move[0]][move[1]] = 2
<<<<<<< HEAD

=======
    l=move[0]
    col=move[1]
>>>>>>> origin/develop
def parcours(ligne,colonne,Vx,Vy,joueur):
    cpt = 0   
    while True:
        ligne+=Vy
        colonne+=Vx
        if((ligne > nb_lignes-1 or ligne < 0) or (colonne > nb_colonnes-1 or colonne < 0)):
            break
        else:
            if(theBoard[ligne][colonne] == joueur):
                cpt+=1
            else:
                break
    return cpt

# Le principe est qu'on vérifie le conformité de la pièce du joueur avec celle suivante
# suivant l'axe, si on trouve une pièce adverse on s'arrete et on passe à l'autre axe, sinon on incrémente le compteur
def checkWinningConditions(ligne,colonne,joueur):
    winning = False
<<<<<<< HEAD
    if(compteur==72):
        print("Egalité")
=======
    if(compteur==42):
        print("__TIE__")
>>>>>>> origin/develop
        winning = None
    victory = 4
    
    # Ligne -
    valeur = parcours(ligne,colonne,1,0,joueur) + parcours(ligne,colonne,-1,0,joueur) + 1 
    if(valeur >= victory):
        print("Ligne -")
        winning = True
    
    # Colonne |
    valeur = parcours(ligne,colonne,0,1,joueur) + parcours(ligne,colonne,0,-1,joueur) + 1
    if(valeur >= victory):
        print("Colonne |")
        winning = True
    
    # Diagonale ascendante /
    valeur = parcours(ligne,colonne,1,1,joueur) + parcours(ligne,colonne,-1,-1,joueur) + 1
    if(valeur >= victory):
        print("Diagonale ascendante /")
        winning = True
    
    # Diagonale descendante \
    valeur = parcours(ligne,colonne,-1,1,joueur) + parcours(ligne,colonne,1,-1,joueur) + 1
    if(valeur >= victory):
        print("Diagonale descendante \"")
        winning = True  
       
    return winning

def PvP():
    joueur = 1
    compteur =1
    gameNotFinished = False
    while not gameNotFinished:
        isPositionNotOkay = True
        print("Tour: "+ str(compteur)+f" Joueur: {joueur}")
        printBoard()
        while isPositionNotOkay:
            userInput = input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour:\n")
            colonne = int(userInput) - 1
            if colonne in np.arange(0,12):
                if canPlay(colonne):
                    ligne = getLastFreeCase(colonne)
                    theBoard[ligne][colonne] = joueur
                    compteur += 1
                    gameNotFinished = checkWinningConditions(ligne, colonne,joueur)
                    isPositionNotOkay = False
                else:
                    print("La case choisi n'est pas valide !")
            else:
                print("La case choisi n'est pas valide !")


        if gameNotFinished is True:
            printBoard()
            print(f"Le joueur {joueur} gagne !")
            break
        elif gameNotFinished is None:
            print("Egalité")
            break
        # Afin de stopper le jeu après que les 42 pièces soit posés
        elif compteur>42:
            printBoard()
            print("Egalité")
            break
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
def PvIA():
    global compteur,l,col
    # print("Qui commence ? (1 : Moi, 2 : IA)")
    playingFirst = False
    gameChoiceIA = None
    while not playingFirst:
        gameChoiceIA = input("Qui commence ? (1 : Moi, 2 : IA)")
        if gameChoiceIA in ["1","2"]:
            playingFirst = True
        else:
            print("Choix inconnu")  
    compteur = 1
    joueur = int(gameChoiceIA)
    gameNotFinished = False
    while not gameNotFinished:
        isPositionNotOkay = True
        print(f"Tour: {compteur} Joueur: {joueur}")
        printBoard()
        if(joueur == 1):
            while isPositionNotOkay:
                userInput = input("Veuillez selectionner une colonne entre 1 et 12 pour valider votre tour:\n")
                colonne = int(userInput) - 1
                if colonne in np.arange(0,12):
                    if canPlay(colonne):
                        ligne = getLastFreeCase(colonne)
                        theBoard[ligne][colonne] = joueur
                        compteur += 1
                        gameNotFinished = checkWinningConditions(ligne, colonne,joueur)
                        isPositionNotOkay = False
                    else:
                        print("Il n'est pas possible de jouer là !")
                else:
                    print("Case hors du plateau !")
        else:
<<<<<<< HEAD
            printBoard()
            turnAI()
            compteur += 1
            gameNotFinished = checkWinningConditions(ligne, colonne,joueur)
=======
            # printBoard()
            turnAI()
            compteur += 1
            gameNotFinished = checkWinningConditions(l, col, compteur,2)
>>>>>>> origin/develop


        if gameNotFinished is True:
            printBoard()
            print(f"Le joueur {joueur} gagne !")
            break
        elif gameNotFinished is None:
            print("Egalité...")
            break
        # Afin de stopper le jeu après que les 42 pièces soit posés
        elif compteur>42:
            printBoard()
            print("Egalité")
            break
        
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
    pass
    
def gameLoop():
    hasChosen = False
    gameChoice = None
    while not hasChosen:
        gameChoice = input("Sélectionnez le mode de jeu : \n 1) Player versus Player \n 2) Player versus IA \n\n")
        if gameChoice in ["1","2"]:
            hasChosen = True
        else:
            print("Choix inconnu")  
    if(gameChoice == "1"):
        print("Choix 1 : Joueur contre Joueur")
        PvP()
    elif(gameChoice == "2"):
        print("Choix 3 : Joueur contre IA")
        PvIA()
  

if __name__ == "__main__":
    gameLoop()
