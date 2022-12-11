player1board = [ #Grille du joueur 1
           #profondeur 1 => X = 0
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ...
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
      #Z --> 0  1  2  3  4 ...
            #profondeur 2 => X = 1
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ...
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            #profondeur 3 X = 2
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # y = 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ...
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
          ]
          #Grille joueur 2
player2board = [ 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ...
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # x = 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ...
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ]
        
        
#Liste des bateaux avec leur longueur
# Bateau SB ==> longueur = 1
# Bateau MB ==> longueur = 2
# Bateau BB ==> longueur = 3



def simple():
    COORDXSB = eval(input("saisir coordonnée x du petit bateau:", ))
    COORDYSB = eval(input("saisir coordonnée y du petit bateau:", ))
    COORDZSB = eval(input("saisir coordonnée Z du petit bateau:", ))
    SB = player1board[COORDXSB][COORDYSB][COORDZSB]
    player1board[COORDXSB][COORDYSB][COORDZSB]= "S" 
    print(player1board)
    
    COORDHEADXMB = eval(input("saisir coordonnée x du petit bateau:", ))
    COORDHEADYMB = eval(input("saisir coordonnée y du petit bateau:", ))
    COORDHEADZMB = eval(input("saisir coordonnée Z du petit bateau:", ))
    COORDTAILXMB = eval(input("saisir coordonnée x du petit bateau:", ))
    COORDTAILYMB = eval(input("saisir coordonnée y du petit bateau:", ))
    COORDTAILZMB = eval(input("saisir coordonnée Z du petit bateau:", ))
    HEAD = player1board[COORDHEADXMB][COORDHEADYMB][COORDHEADZMB]
    TAIL = player1board[COORDTAILXMB][COORDTAILYMB][COORDTAILZMB]
    LONGUEUR = int(input())
    LONGUEUR = len([[HEAD],[TAIL]])
    def pose_mb (LONGUEUR, HEAD, TAIL):
        for i in range(LONGUEUR):
            if HEAD == 'S':
                return False
            elif TAIL == 'S':
                return False
        return True
    
    
    MB = player1board[COORDHEADXMB][COORDHEADYMB][COORDHEADZMB]

def complexe():
    
    longueur = 0 #int(input("entrer la longueur du bateau:", ))
    orientation = " " #input("choisissez entre vertical ou horizontal:",)
    x = 0 #int(input("entrer coordonnée x du bateau:", ))
    y = 0 #int(input("entrer coordonnée y du bateau:", ))
    z = 0 #int(input("entrer coordonnée z du bateau:", ))
    
    def verif_emplacement(player1board, longueur, orientation, x, y, z):
        try:  
            for i in range(longueur):
                if orientation == 'horizontal':
                    if player1board[x][y][z+i] == 'S': 
                        print("la case est deja prise veuiller reprendre la saisie")
                        return False

                elif orientation == 'vertical':
                    if player1board[x][y+i][z] == 'S': 
                        print("la case est deja prise veuiller reprendre la saisie")
                        return False
                    
        except IndexError:
            return False
        return True

    #verif_emplacement(player1board, longueur, orientation, x, y)

    def pose_bateau(player1board, verif_emplacement, longueur, nom, x, y, z):
        if verif_emplacement(player1board, longueur, orientation, x, y, z):
            for i in range(longueur):
                if orientation == 'horizontal':
                    player1board[x][y][z+i] = nom
                    player1board[x][y][z+i] = "S"
                if orientation == 'vertical':
                    player1board[x][y+i][z] = nom
                    player1board[x][y+i][z] = "S"
    nom = "SB"                
    pose_bateau(player1board, verif_emplacement, longueur, nom, x, y, z)

    bateaux_posés = set()
    while len(bateaux_posés) < 3: # 3 bateaux
        x = int(input("x :"))
        y = int(input("y :"))
        z = int(input("z :"))
        orientation = input("orientation :")
        nom = input("nom :")
        longueur = int(input("longueur :"))
        pose_bateau(player1board, verif_emplacement, longueur, nom, x, y, z)
        bateaux_posés.add(nom) 

    print(bateaux_posés)
    print(player1board)

switch = {1 : simple, 2 : complexe}
x = int(input("veuiller choisir le numéro de la fonction à executer : \n" "1 = simple ; 2 = complexe \n" ": ",))
if x == 1:
    switch.get(x, simple)()
elif x == 2:
    switch.get(x, complexe)()
