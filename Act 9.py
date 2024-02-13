#BENYAHIA Ilyas 21118889




exemple1 : List[str] = ['Je suis belle, ô mortels ! comme un rêve de pierre,\n',
                        "Et mon sein, où chacun s'est meurtri tour à tour,\n",
                        'Est fait pour inspirer au poète un amour\n',
                        'Éternel et muet ainsi que la matière.\n',
                        '\n',
                        "Je trône dans l'azur comme un sphinx incompris ;\n",
                        "J'unis un coeur de neige à la blancheur des cygnes ;\n",
                        'Je hais le mouvement qui déplace les lignes,\n',
                        'Et jamais je ne pleure et jamais je ne ris.\n',
                        '\n',
                        'Les poètes, devant mes grandes attitudes,\n',
                        "Que j'ai l'air d'emprunter aux plus fiers monuments,\n",
                        "Consumeront leurs jours en d'austères études ;\n",
                        '\n',
                        "Car j'ai, pour fasciner ces dociles amants,\n",
                        'De purs miroirs qui font toutes choses plus belles :\n',
                        'Mes yeux, mes larges yeux aux clartés éternelles !']


def ouvre_fichier(nom : str) -> List[str] :
    """ renvoie la liste des lignes du fichier texte ./nom.txt """
    with open("./"+nom+".txt", "r", encoding = "utf-8") as f:
        return f.readlines()


lettres_francais : Dict[str, float] = {"e" : 0.1210,
                                       "a" : 0.0711,
                                       "i" : 0.0659,
                                       "s" : 0.0651,
                                       "n" : 0.0639,
                                       "r" : 0.0607,
                                       "t" : 0.0592,
                                       "o" : 0.0502,
                                       "l" : 0.0496,
                                       "u" : 0.0449,
                                       "d" : 0.0367,
                                       "c" : 0.0318,
                                       "m" : 0.0262,
                                       "p" : 0.0249,
                                       "é" : 0.0194,
                                       "g" : 0.0123,
                                       "b" : 0.0114,
                                       "v" : 0.0111,
                                       "h" : 0.0111,
                                       "f" : 0.0111,
                                       "q" : 0.0065,
                                       "y" : 0.0046,
                                       "x" : 0.0038,
                                       "j" : 0.0034,
                                       "è" : 0.0031,
                                       "à" : 0.0031,
                                       "k" : 0.0029,
                                       "w" : 0.0017,
                                       "z" : 0.0015,
                                       "ê" : 0.0008,
                                       "ç" : 0.0006,
                                       "ô" : 0.0004,
                                       "â" : 0.0003,
                                       "î" : 0.0003,
                                       "û" : 0.0003,
                                       "ù" : 0.0003,
                                       "ï" : 0.0001}

ponctuation : Set[str] ={" ", ",", ";", "’", "(", ")", ".", "!", "?", ":"}
                         
                         
def decompose_ligne(li:str, sep:Set[str])->List[str]:
    """renvoie la liste "li" choisi, découpé selon le caractère "sep"."""
    lr:List[str] = []
    c:str
    mot:str=""
    for c in li:
        if c in  sep or c == "\n":
            lr.append(mot)
            mot=""
        else:
            mot=mot+c
    return lr
assert decompose_ligne(exemple1[4], ponctuation)==['']
assert decompose_ligne(exemple1[8], ponctuation)==['Et', 'jamais', 'je', 'ne', 'pleure', 'et', 'jamais', 'je', 'ne', 'ris', '']

import math

#question2
def minusculise(mot:str)->str:
    """
    """
    mot1:str=''
    e:str
    for e in mot:
        if e >= 'A' and e<='Z':
            e=chr(ord(e)+32)
            mot1=mot1+e
        else:
            mot1=mot1+e
    return mot1

#   65 -> 90 Majuscules
#   97 -> 122 minuscules
assert minusculise("bonjour")=="bonjour"
assert minusculise("BONJOUR")=="bonjour"

#Question3
def mots(lis:List[str],sep:Set[str])->List[str]:
    """
    """
    return [minusculise(mot) for li in lis for mot in decompose_ligne(li,sep)]


assert mots(exemple1 , ponctuation)[:15]==['je', 'suis', 'belle', '', 'ô', 'mortels', '', '', 'comme', 'un', 'rêve', 'de', 'pierre', '', 'et']


#Question4

    



