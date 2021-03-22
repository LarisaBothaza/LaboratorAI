
from random import randint, seed
import math

def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm

def readFromFile(file):
#un cromozom = drumu
#un oras = nod
    fisier = open(file, 'r')

    n = int(fisier.readline())        #first line: number of cities (n)
    costOrase = []
        #second - n + 1 line: distances between the k-th city and all the other cities (n real values)
    for index in range(0,n):
        costuri = []
        for numar in fisier.readline().split(','):
             costuri.append(int(numar))
        costOrase.append(costuri)

    fisier.close()
    return n, costOrase

def distEuclid(Xa,Xb,Ya,Yb):
    return math.sqrt(pow((Xa-Xb),2)+pow((Ya-Yb),2))

def readFromFileHard(file):
#un cromozom = drumu
#un oras = nod
    fisier = open(file, 'r')

    n = int(fisier.readline())        #first line: number of cities (n)
    #auxiliar matrice cu datele citite, fiecare linie are coordonate
    auxiliar = []
    for i in range(n):
        coordonate = []
        for date in fisier.readline().split(','):
            coordonate.append(float(date))  #0: nod, 1:Xa, 2: Xb
        auxiliar.append(coordonate)     

    #matricea costurilor
    matrice = []
    for i in range(n):
        linie = []
        for j in range(n):
            distanta = distEuclid(auxiliar[i][1],auxiliar[i][2],auxiliar[j][1],auxiliar[j][2])
            linie.append(distanta)
        matrice.append(linie)

    fisier.close()
    return n, matrice

def fitness(vectorRepres, matriceCost): #calitatea cromozomului
    #vectorRepres = cromozomii
    #vectorRepres = matricea de adiacenta 
    #calculeaza costu pentru 
    cost = 0
    n = len(vectorRepres)-1

    for i in range(0,n):

        cost += matriceCost[vectorRepres[i]][vectorRepres[i+1]] #din maricea de costuri

    cost += matriceCost[vectorRepres[n]][vectorRepres[0]] #pentru ca se intoarce de unde a pornit

    return cost