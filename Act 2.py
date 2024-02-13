import math
import random
#ACT 2
print("Hello World")
#2

def terme_leibniz(n:int)->float:
    """"""
    return ((-1)**n) / (2*n+1)

assert terme_leibniz (0) == 1
assert terme_leibniz (1) == -1/3
assert terme_leibniz (10) == 1 / 21

def somme_leibniz(n:int)->float:
    """"""
    s:float = 0
    u:int = n
    while u >= 0:
        s = s + terme_leibniz(u)
        u = u - 1
    return s

assert somme_leibniz(0) == 1
assert somme_leibniz(1) == 1 - 1 / 3
assert somme_leibniz(4) == 0.834920634920635

def approx(n:int)->float:
    """"""
    return somme_leibniz(n)*4

assert abs(approx(1) - math.pi) < 10**0
assert abs(approx(100) - math.pi) < 10**0
assert abs(approx(1000) - math.pi) < 10**(-2)

def factorielle(n:int)->int:
   if n == 0:
      return 1
   else:
      f:int = 1
      k:int
      for k in range(2,n+1):
         f = f * k
      return f

def mq(q:int)->float:
    """"""
    return factorielle(6*q)/((factorielle(3*q)*(factorielle(q))**3))

def lq(q:int)->float:
    """"""
    return 545140124*q + 13591409
    

def xq(q:int)->float:
    """"""
    return(-262537412640768000)**q

def approx_chudnovsky(q:int)->float:
    """"""
    c:float
    c = 426880*(math.sqrt(10005))
    n:int = q
    s:float = 0
    while n >=0:
        s = s + (( mq(n) * lq(n) )/ xq(n))
        n = n-1
    return (s**(-1))*c

def approx_aleatoire(n:int)->float:
    u:int = n
    c:int = 0
    while u>=0:
        pa:float = random.random()
        pb:float = random.random()
        if abs(math.sqrt((pa - 0.5)**2 + (pb - 0.5)**2)) <= 0.5:
               c = c + 1
        u = u - 1
    return c/n

#Recherches
#Suite de héron , approximation d'une racine d'un nombre
def heron(a,p):
    u = 3 # premier terme
    N = ceil( log( log( 10**p , 2) + 1 , 2) )
    for n in range(N):
        u = 0.5 * (u + a/u)    
    return u,N

