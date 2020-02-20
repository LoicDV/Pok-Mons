
import sys


def read(file):
    with open(file, "r") as f:
        first = f.readline().strip()
        books, libr, days = first.split(" ")
        books, libr, days = int(books), int(libr), int(days)
        scores = f.readline().strip().split(" ")
        list_libr = []
        for i in range(libr):
            # gérer la biblio numéro i
            # Le nombre de livres, biblio et de jours
            # sont dans les var "books", "libr" et "days"
            config1 = f.readline().strip().split(" ")
            config2 = f.readline().strip().split(" ")
            list_libr.append((config1, config2))

        return (books, libr, days, scores, list_libr)



if __name__ == "__main__":

    t = read(sys.argv[1])
    print(t)
    """
     t a 5 éléments. Le premier est le nb de livre, second est le nb de bibli
     le 3ème est le nb de jours
     Le 4ème est une liste où l'élément à la place i est le score du livre i
     Le 5ème une liste où l'élément à la place i est la bibliothètque i :
        la bibli i est un tuple de 2 éléments :
            1er : (nb livres dedans, nb de jour pour signup, livre par jours)
            2eme : liste des id des livres dispo
    """