import random


def jatek(n):

    lehetosegek = ['Kő', 'Papír', 'Olló']

    korok = ''
    i = 0
    p1 = 0
    p2 = 0
    while i < n:
        r1 = random.randint(0, 2)
        r2 = random.randint(0, 2)

        if lehetosegek[r1] == "Kő" and lehetosegek[r2] == "Papír":
            p2 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i+1, lehetosegek[r1], lehetosegek[r2], 2)
            i += 1
        elif lehetosegek[r1] == "Kő" and lehetosegek[r2] == "Olló":
            p1 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 1)
            i += 1
        elif lehetosegek[r1] == "Papír" and lehetosegek[r2] == "Olló":
            p2 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 2)
            i += 1
        elif lehetosegek[r1] == "Papír" and lehetosegek[r2] == "Kő":
            p1 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 1)
            i += 1
        elif lehetosegek[r1] == "Olló" and lehetosegek[r2] == "Kő":
            p2 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 2)
            i += 1
        elif lehetosegek[r1] == "Olló" and lehetosegek[r2] == "Papír":
            p1 += 1
            korok += "{}. forduló: {}\t|\t{}\t{}. játékos nyert.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 1)
            i += 1
        else:
            korok += "{}. forduló: {}\t|\t{}\tDöntetlen.\n".format(i + 1, lehetosegek[r1], lehetosegek[r2], 2)
            i += 1
            n += 1

    if p1 > p2:
        return "1. játékos nyert.\n\n" + korok
    else:
        return "2. játékos nyert.\n\n" + korok

n=int(input("Adja meg a fordulók számát: "))
print(jatek(n))