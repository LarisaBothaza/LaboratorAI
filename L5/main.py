from utils import *
from random import *

from ACO import ACO
from Ant import Ant
   
lengthGraph , graph = readFromFile('normal.txt')  
# lengthGraph, graph = readFromFileCoord('euclid.txt') 

            #( nr furnici in colonie , nr iteratii, coeficient 1, coeficient 2, constanta evaporare, constanta alegere oras nou)
acoParams = {'colSize': 10, 'noGen':100, 'alpha':1, 'beta':10, 'evaporation':0.4, 'probQ':0.4}
    #colSize - se plasează aleator m furnici in cele n noduri-oras (m <= n)
    #aplha - controlează importanţa urmei (câte furnici au mai trecut pe muchia respectivă)
    #beta - controlează importanţa vizibilităţii (cât de aproape se află următorul oraş)

                #( matricea de adiacenta, nr noduri, matricea cu feromoni )
problemParams = {'network':graph, 'noNodes': lengthGraph, 'feromons': [[0] * lengthGraph] * lengthGraph}

def main():

    aco = ACO(acoParams, problemParams)

    theBestBest = []
    theBestCost = 999999999
    gen = 0

    for generation in range(acoParams['noGen']):

        aco.initialisation()

        #DINAMIZARE GRAF: graful static asupra caruia se aplica diferite perturbari random
        nodes = problemParams['noNodes']
        prob = uniform(0,1)
        if prob < 0.4:
            i = randint(0, nodes-1)
            j = randint(0, nodes-1)
            perturbare = uniform(1,2)
            problemParams['network'][i][j] *= perturbare
            problemParams['network'][j][i] //= perturbare

        for step in range(problemParams['noNodes'] - 1):
            aco.oneStepAnt()      # fiecare furnica face o mutare/un pas

        aco.goHomeAnts()

        #Ant system: Toate furnicile depun feromon după construirea unei soluţii complete (modificare globală colectivă)
        aco.updateFeromons() #matricea colectiva cu feromon

        bestAnt = aco.bestAnt()
        print('Generatia: ' + str(generation+1) + ' ' + str(bestAnt.path) + ' cost: ' + str(bestAnt.cost))

        if bestAnt.cost < theBestCost:
            theBestCost = bestAnt.cost
            theBestBest = bestAnt.path
            gen = generation+1

    print('\nOverall the best: ' + str(gen) + ' ' + str(theBestBest) + ' cost: ' + str(theBestCost) )

main()
