def divise(k : int, n : int) -> bool :
    """ Pre : k > 0 and n >= 0
    Decide si k divise n """

    return n % k == 0

def est_parfait(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait."""

    s : int = 0
    i : int = 1
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
    return n == s

def est_parfait_opti(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """

    s : int = 1
    i : int = 2
    if i == 1 : 
        return False
    while i != int(math.sqrt(n)) + 1 :
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i = i + 1
    return n == s