Polyn = List[int]
ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1,-1 ,1 ,-1 ,0]
ex3 : Polyn = [27]
ex4 : Polyn = []

def degre(l:List[int])->int:
    """"""
    i:int
    for i in range(1, len(l)):
        if l[-i] != 0:
            return len(l) -i
    return 0

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre(ex4) == 0
assert degre([0,0,0,0,0]) == 0

def somme(l1:List[int] , l2:List[int])->List[int]:
    """"""
    i:int
    lr:List[int] = []
    if l2 == []:
        return l1
    for i in range (0, len(l1)):
        lr.append(l1[i] + l2[i])
    j:int
    for j in range ( len(l1) , len(l2)):
        lr.append(l2[j])
    return lr

assert somme(ex1, ex1) == [6, 0, 4]
assert somme(ex1, ex4) == ex1
assert somme(ex1, ex2) == [4, -1 , 3 , -1 ,0]

def normalise(l:List[int])->List[int]:
    """"""
    i:int
    lr:List[int] = []
    if degre(l) == 0:
        return lr
    for i in range (0 , degre(l)+1):
        lr.append(l[i])
    return lr

assert normalise(ex1) == ex1
assert normalise(ex2) == [1, -1, 1, -1]
assert normalise([0,0,0,0,0]) == []
assert normalise([]) == []

def produit(l1:List[int] , l2:List[int]) -> List[int]:
    """"""
    n:int
    lr:List[int] = []
    for n in l1:
        m:int
        for m in l2:
            lr.append(n*m)
    return lr

#2
def multiplie(l:List[int] , k:int)->List[int]:
    """"""
    i:int
    lr:List[int] = []
    for i in l:
        lr.append(i*k)
    return lr

def derive(l:List[int])-> List[int]:
    """"""
    i:int
    lr:List[int] = []
    for i in range (1,len(l)):
        lr.append(l[i]*i)
    return lr

assert normalise(derive(ex1)) == [0, 4]
assert normalise(derive(ex4)) == []
assert normalise(derive(ex2)) == [-1,2,-3] 

def integrale(l:List[int])-> List[float]:
    """"""
    i:int
    lr:List[float] = []
    lr.append(0)
    for i in range (0,len(l)):
        lr.append(l[i]/(i+1))
    return lr

#3
def valeur(l:List[int],x:float)->float:
    """"""
    i:int
    if l == []:
        return 0
    s:float = l[0]
    for i in range(1,len(l)):
        s = s + l[i]*(x**(i))
    return s

assert valeur(ex1, 0) == 3
assert valeur(ex1, -1)== 5
assert valeur(ex4, 2.5) == 0

def cdp(l:List[int])->str:
    """"""
    c:str = ''
    i:int
    for i in range(1,len(l)+1):
        if l[-i] != 0:
            if l[-i] < 0:
                c = c + '-'+ str(l[-i])+'.X^'+str(len(l)-i+1)
            elif l[-i] > 0:
                c = c + '+' + str(l[-i])+'.X^'+str(i)
    return c
