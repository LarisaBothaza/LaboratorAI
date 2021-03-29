from math import sqrt

def readFromFile(filename):

    fisier = open(filename, 'r')

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

def distEuclid(a, b):
    return sqrt(pow((a[0]-b[0]),2)+pow((a[1]-b[1]),2))

def readFromFileCoord(filename):
    
    auxiliar = []

    with open(filename, 'r') as file:
        
        #citire dimensiune
        line = file.readline().strip().split(':')
        while line[0].strip(' ') != 'DIMENSION':
            line = file.readline().strip().split(':')

        n = int(line[1])

        #pentru a trece de cele 2 linii si a ajunge la noduri
        file.readline()
        file.readline()

        for i in range(n):
            line = file.readline().strip().split(' ')

            coordonate = []
            coordonate.append(float(line[1]))
            coordonate.append(float(line[2]))

            auxiliar.append(coordonate)
 
    costOrase = []
    for oras1 in range(n):
        linie = []

        for oras2 in range(n):
            distanta = distEuclid(auxiliar[oras1], auxiliar[oras2])
            linie.append(distanta)

        costOrase.append(linie)
           
    return n, costOrase




