
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

def tri_book(big):
    id_books = big[4][1]
    nombre = big[0]
    score_books = big[3]
    t = []
    i = 0
    while len(t) != len(id_books):
        tmp = id_books[i]
        liste = [score_books[tmp], tmp]
        t.append(liste)
        t.sort(reverse=True)
    res = []
    for i in range(len(t)):
        res[i] = t[i][1]
    return res

def isIn(bibli, book):
    t = bibli[1]
    for i in range (len(t)):
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
    longueur = len(liste)
    for i in range(longueur):
        if isIn(liste[i]):
            rm(liste[i], book)
            #TODO niveau score

def write(data, values, name="output.txt"):
    with open(name, 'w') as f:
        f.write(str(data[1])+"\n")
        for k in range(len(values)):
            best_lib = values.index(max(values))
            f.write(str(best_lib) + " " + str(data[4][best_lib][0][0]) + "\n")

            f.write('output books\n')

            values[best_lib] = -42



if __name__ == "__main__":

    data = read(sys.argv[1])
    values_of_lib = []

    for i in range(data[1]):
        temp = sumValBooksInLib_i(data, i)
        moyenne = temp[0]/temp[1]
        livre_par_jour = data[4][i][0][2]
        output_moy = moyenne * livre_par_jour
        signup = data[4][i][0][1]
        duree_vie = data[4][i][0][0] / livre_par_jour

        if duree_vie > data[2]:
            VALUE = 0
        else:
            VALUE = (output_moy*duree_vie) / ((signup/10)+1)
        values_of_lib.append(VALUE)
        # print(i, "|", VALUE, "|", output_moy, "|", signup, "|", duree_vie)

    name = sys.argv[1]
    write(data, values_of_lib, name=name[:len(name)-4]+"_output.txt")


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