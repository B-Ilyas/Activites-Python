#BENYAHIA Ilyas 21118889

def somme_totale(n:int)->int:
    """"""
    if n==0:
        return 0
    else:
        return n+somme_totale(n-1)

assert somme_totale(5)==15
assert somme_totale(6)==21
assert somme_totale(7)==28


Coord = Tuple[int, int]
Dir = str

ori : Coord = (0, 0)
p1 : Coord = (3, 3)
p2 : Coord = (0, 2)


#Q1:
def deplace(c:Coord, d:Dir)->Coord:
    """ """
    x, y=c
    if d=='N':
        return (x, y+1)
    elif d=='S':
        return (x, y-1)
    elif d=='E':
        return (x+1, y)
    elif d=='O':
        return (x-1, y)
assert deplace(ori, "N") == (0, 1)
assert deplace(p1, "E") == (4, 3)
assert deplace(deplace(p2, "N"), "S") == p2

#Q2
def deplace_chemin(c:Coord,ch:List[Dir])->Coord:
    """ """
    if ch==[]:
        return c
    else:
        return deplace_chemin(deplace(c, ch[0]),ch[1:])
assert deplace_chemin(ori,["N", "N"]) == p2
assert deplace_chemin(ori,["N", "E", "S", "O"]) == ori
assert deplace_chemin(ori,[]) == ori


Case = Tuple[bool,bool,bool,bool,str]
Laby = List[List[Case]]
laby1 : Laby = [[(True,True,False,False, ""),
                 (False,False,True,False, "ENTREE")],
                [(True,False,False,True, ""),
                 (False,False,True,False, "SORTIE")]]

laby2 : Laby = [[(True,False,False,False, ""),
                 (False,True,True,False, ""),
                 (True,True,False,False, ""),
                 (False,False,True,False, "ENTREE")],
                [(False,False,False,False, ""),
                 (True,True,False,True, ""),
                 (True,False,True,True, ""),
                 (False,True,True,False, "")],
                [(True,False,False,False, ""),
                 (False,False,True,True, ""),
                 (True,True,False,False, ""),
                 (False,False,True,True, "")],
                [(True,False,False,False, "SORTIE"),
                 (True,False,True,False, ""),
                 (True,False,True,True, ""),
                 (False,False,True,False, "")]
                ]

#Q3
def deplace_possible(la:Laby,c:Coord, d:Dir)->bool:
    """ """
    x, y=c
    n,e,s,o,_=la[x][y]
    
    if d=='N':
        return n
    elif d=='S':
        return s
    elif d=='E':
        return e
    elif d=='O':
        return o
assert deplace_possible(laby1, (0, 1), "S")
assert not deplace_possible(laby1, (0, 1), "N")
assert not deplace_possible(laby1, (0, 1), "E")

#Q4
def chemin_possible(la:Laby,c:Coord,ch:List[Dir])->bool:
    """ """
    if ch==[]:
        return True
    elif not deplace_possible(la, c, ch[0]):
        return False
    else:
        return chemin_possible(la, deplace(c, ch[0]), ch[1:])

assert chemin_possible(laby1, (0, 1), ["S", "E", "N"])
assert chemin_possible(laby1, (0, 1), ["S", "N", "S", "E", "N"])
assert not chemin_possible(laby1, (0, 1), ["S", "O"])
assert not chemin_possible(laby1, (0, 1), ["S", "E", "N", "O"])






