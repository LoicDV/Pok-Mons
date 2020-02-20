
import sys


def read(file):
    with open(file, "r") as f:
        first = f.readline().strip()
        books, lib, days = first.split(" ")
        books, lib, days = int(books), int(lib), int(days)
        scores = list(map(int, f.readline().strip().split(" ")))
        list_lib = []
        for i in range(lib):
            # gérer la biblio numéro i
            # Le nombre de livres, biblio et de jours
            # sont dans les var "books", "libr" et "days"
            config1 = list(map(int, f.readline().strip().split(" ")))
            config2 = list(map(int, f.readline().strip().split(" ")))
            list_lib.append((config1, config2))

        return (books, lib, days, scores, list_lib)

def isIn(bibli, book):
    t = bibli[1]
    for i in range (len(t)- 1):
        if (t[i] == book):
            return True
    return False

def rm(bibli, book):
    t = bibli[1]
    verif = False
    i = 0
    while (i != len(t)) and (verif == False):
        if (t[i] == book):
            t.remove(book)
            verif = True
        i += 1

def refresh(big, book):
    liste = big[4]
    longueur = len(liste) - 1
    for i in range(longueur):
        if isIn(liste[i]):
            rm(liste[i], book)
            #TODO niveau score

def sumValBooksInLib_i(data, i):
    """
    return un tuple de 2 elements :
    0 : La somme du score des livres dans la biblio i
    1 : le nombre total de livres dans la biblio i
    """
    lib = data[4][i]
    res = 0
    for k in lib[1]:
        res += data[3][k]
    return (res, lib[0][0])


if __name__ == "__main__":

    data = read(sys.argv[1])
    for i in range(data[1]):
        print(sumValBooksInLib_i(data, i))
    """
    data a 5 éléments :
       0 : le nb de livre
       1 : le nb de bibli
       2 : le nb de jours
       3 : liste où l'élément à la place i est le score du livre i
       4 : liste où l'élément à la place i est la bibliothèque i :
          la bibli i est un tuple de 2 éléments :
            0 : tuple de 3 éléments :
                0 : nb livres dedans
                1 : nb de jour pour signup
                2 : livres par jours
            1 : liste des id des livres dispo
    """