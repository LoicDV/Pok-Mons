
import sys


def read(file):
    with open(file, "r") as f:
        first = f.readline().strip()
        books, libr, days = first.split(" ")
        books, libr, days = int(books), int(libr), int(days)
        scores = f.readline().strip().split(" ")
        for i in range(libr):
            # gérer la biblio numéro i
            # Le nombre de livres, biblio et de jours
            # sont dans les var "books", "libr" et "days"
            f.readline()
            f.eadline()


if __name__ == "__main__":

    read(sys.argv[1])