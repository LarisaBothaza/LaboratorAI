#Traveling Salesperson

import os.path
LIMIT_MIN = 999999999

#citeste datele din fisier
#parametri: input: caleFisierCitire
#           output: n(INT), orasSursa(INT), orasDestinatie(INT), costOrase (matrice[INT][INT])
# n - numarul de orase 
# costOrase - matrice cu costul oraselor 
def citesteDate(caleFisierCitire):
    if not os.path.isfile(caleFisierCitire):
        print('Fisierul nu exista!')
    else:
        fisier = open(caleFisierCitire, 'r')

        n = int(fisier.readline())        #first line: number of cities (n)
        costOrase = []
        #second - n + 1 line: distances between the k-th city and all the other cities (n real values)
        for index in range(0,n):
            costuri = []
            for numar in fisier.readline().split(','):
                costuri.append(int(numar))
            costOrase.append(costuri)

        orasSursa = int(fisier.readline())           #index of source city
        orasDestinatie = int(fisier.readline())      #index of destination city
        fisier.close()
        return n, orasSursa, orasDestinatie, costOrase

#returneaza pozitia si costul minim, orasul care urmeza sa fie vizitat
#parametri: input:n(INT), distanteOrase (vector[INT]), vectorVizitat(vector[INT])
#           output:pozitie_minim(INT), costMinim(INT)
def detUrmator(n, distanteOrase, vectorVizitat):
    pozitie_minim = -1
    costMinim = LIMIT_MIN
    
    for index in range(0,n):
        if index+1 not in vectorVizitat:
            if distanteOrase[index] != 0 and distanteOrase[index] < costMinim :
                pozitie_minim = index+1
                costMinim = distanteOrase[index]

    return pozitie_minim, costMinim  

#determina drumul de cost minim de la orasSursa la orasDestinatie
#parametri: input: n(INT), orasSursa(INT), orasDestinatie(INT),costOrase (matrice[INT][INT])
#           output: (INT) numarul de orase, (vector[INT]) drumul gasit, (INT) costul total 
def detDrumCostMin(n, orasSursa, orasDestinatie, costOrase):
    vectorVizitat = [orasSursa]
    costTotal = 0

    for oras in range(0,n):
        if(len(vectorVizitat) != n):
            pozitie_minim, costMinim = detUrmator(n, costOrase[vectorVizitat[-1]-1], vectorVizitat)
            vectorVizitat.append(pozitie_minim)
            costTotal = costTotal + costMinim

        if(pozitie_minim == orasDestinatie):        #pentru cerinta 2 se va aplica
            break

    if orasSursa == orasDestinatie:
        costTotal = costTotal + costOrase[vectorVizitat[-1]-1][vectorVizitat[0]-1]

    return len(vectorVizitat), vectorVizitat, costTotal
            

def run():
    caleFisierCitire = 'D:/UBB_sem4/AI/Laborator/LaboratorAI/L2/greedy.txt'
    caleFisierAfisare = 'D:/UBB_sem4/AI/Laborator/LaboratorAI/L2/greedy_solution.txt'
    n, orasSursa, orasDestinatie, costOrase = citesteDate(caleFisierCitire)

    #determinare drum cerinta 1 - ciclu: nod sursa = nod destinatie
    minim = LIMIT_MIN
    theBest = []
    for index in range(0,n+1):
        if index != 0:
            n,vectorVizitat,costTotal = detDrumCostMin(n, index, index, costOrase)
            if costTotal < minim:
                minim = costTotal
                theBest = vectorVizitat

    #print(n), print(theBest), print(minim)
    
    #afisare in fisier 
    outF = open(caleFisierAfisare,'w')
    #cerinta 1: ciclu: nod sursa = nod destinatie
    outF.write(str(n))
    outF.write('\n')
    for nr in theBest[:-1]:
        outF.write(str(nr)+',')
    outF.write(str(theBest[-1]))
    outF.write('\n')
    outF.write(str(minim))
    outF.write('\n')

    #cerinta 2: nod sursa != nod destinatie
    minn,vectorVizitat,costTotal = detDrumCostMin(n, orasSursa, orasDestinatie, costOrase)
    #afisare in fisier: cerinta 2
    outF.write(str(minn))
    outF.write('\n')
    for nr in vectorVizitat[:-1]:
        outF.write(str(nr)+',')
    outF.write(str(vectorVizitat[-1]))
    outF.write('\n')
    outF.write(str(costTotal))
    outF.close()

    print("Gata!")

run()
