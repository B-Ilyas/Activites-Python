#BENYAHIA Ilyas 21118889
exemple1 : List[str] = ['"sport";"date";"participants";"vainqueur"\n',
                        '"boxe";"2021-09-18";"12";"Alice"\n',
                        '"boxe";"2021-09-25";"10";"Alice"\n',
                        '"karate";"2021-09-26";"19";"Carole"\n',
                        '"boxe";"2021-10-02";"8";"Bob"\n',
                        '"karate";"2021-10-03";20;"Carole"\n',
                        '"tennis";"2021-10-04";"3;"Alice"\n',
                        '"boxe";"2021-10-09";"5";"Alice"\n',
                        '"karate";"2021-10-10";"20";"Damien"\n',
                        '"boxe";"2021-10-16";"6";"Carole"\n',
                        '"echecs";"2021-09-17";"120";"Bob"\n',
                        '"echecs";"2021-09-24";"120";"Bob"\n',
                        '"echecs";"2021-10-01";"120";"Carole"\n']

def ouvre_fichier(nom : str) -> List[str] :
    """ renvoie la liste des lignes du fichier texte ./nom.csv """
    with open("./"+nom+".csv", "r") as f:
        return f.readlines()

#Question 1:   
def decompose_ligne(li:str, sep:str)->List[str]:
    """renvoie la liste "li" choisi, découpé selon le caractère "sep"."""
    lr:List[str] = []
    c:str
    mot:str=""
    for c in li:
        if c == sep or c == "\n":
            lr.append(mot)
            mot=""
        else:
            mot=mot+c
    return lr
assert decompose_ligne(exemple1[0], ";")==['"sport"', '"date"', '"participants"', '"vainqueur"']
assert decompose_ligne(exemple1[3], ";")==['"karate"', '"2021-09-26"', '"19"', '"Carole"']
assert decompose_ligne(exemple1[3], ",")==['"karate";"2021-09-26";"19";"Carole"']

#Question 2:
def enleve_guillemets(s:str)->str:
    """renvoie la chaine de caractère en retirant les guillemets."""
    sr:str=""
    c:str
    for c in s:
        if c == '"':
            sr=sr
        else:
            sr=sr+c
    return sr
assert enleve_guillemets('"sport"')=='sport'
assert enleve_guillemets('sport')=='sport'

#Question 3:
def enleve_guillemets_ligne(li:List[str])->List[str]:
    """renvoie une liste en retirant les guillemtes."""
    return [enleve_guillemets(c) for c in li]
assert enleve_guillemets_ligne(['"sport"', '"date"', '"participants"', '"vainqueur"'])==['sport', 'date', 'participants', 'vainqueur']
assert enleve_guillemets_ligne(['"karate"', '"2021−09−26"', '"19"', '"Carole"'])==['karate', '2021−09−26', '19', 'Carole']
