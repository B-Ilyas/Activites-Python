#BENYAHIA Ilyas 21118889

#1 Partie Guidée :  Le Tic-Tac-Toe
#Question 1:

CaseT =str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

def plateau_vide()->PlateauT:
    """
    Renvoie un plateau de jeu vide pour le tic-tac-toe (de taille 3×3, donc).
    """
    return [[" " for i in range(3)] for j in range(3)]
pla1:PlateauT=plateau_vide()

assert pla1[1][1] == " "
assert pla1[0][2] == " "


#Question 2 :

def videt(pla:PlateauT,i:int,j:int)->bool:
    """i,j [0,2]
    Décide si la case de coordonées (i,j) du plateau est vide.
    """
    return pla[i][j]== " "
assert videt(pla1, 1, 1) ==True
assert videt(pla1, 0, 2) ==True


#Question 3 :
def jouex(pla:PlateauT,i:int,j:int)->None:
    """****Procédure***"""
    pla[i][j]== "X"

def joueo(pla:PlateauT,i:int,j:int)->None:
    """***Procédure***"""
    pla[i][j]== "O"

assert videt(pla1, 0, 2)
assert jouex(pla1, 1, 1) == None
assert joueo(pla1, 0, 2) == None
assert not videt(pla1, 0, 2) == False

#Question 4 :
def dessine_plateaut(pla:PlateauT)->str:
    """
    Renvoie une chaine de caractère correspondant à un affichage du plateau :  la case (0,0)  étant en bas à gauche.
    """
    l:List[str]
    i:int
    chaine:str = ''
    debut:str = '/---\\\n'
    for l in pla:
        for i in range(len(l)) :
            if i == 0:
                chaine = chaine + "|"
            chaine = chaine +l[-i-1]
            if i == len(l) -1:
                chaine = chaine + "|"
        chaine = chaine +'\n'    
    fin : str = '\---/'
    print(pla)
    return debut + chaine + fin

pl : PlateauT = [["X"," ","0"],[" ","X"," "],[" "," ", "0"]]    
assert dessine_plateaut(pla1) == '/---\\\n|   |\n|   |\n|   |\n\\---/'
assert dessine_plateaut(pl) == '/---\\\n|0 X|\n| X |\n|0  |\n\\---/'


#Question 5 :
#def gagnet(pl
