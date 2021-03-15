from GA import GA
from random import randint
import networkx as nx
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 
import warnings 

def readFromFile(filename): #fisier.gml
    G = nx.read_gml(filename, label='id')
    net = {}
    net['noNodes'] = G.number_of_nodes()
    net['mat'] = nx.adjacency_matrix(G).todense() 
    net['noEdges'] = G.number_of_edges()
    net['degrees'] = [val for (node, val) in G.degree()]
    net['graph'] = G
    return net

def fitness(communities, param): #calitatea cromozomului
    #lab03/communityDetection/communityGAlive.ipynb: In [6]
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for index in range(0, noNodes):
        for secondIndex in range(0, noNodes):
            if (communities[index] == communities[secondIndex]):
                Q += (mat.item(index,secondIndex) - degrees[index] * degrees[secondIndex] / M)
    return Q * 1 / M

net = readFromFile('adjnoun.gml')
gaParam = {"popSize": 500, "noGen": 5, "network": net}  #cu cat creste pozSize, creste fitnesul
problParam = {'function': fitness, 'retea': net}

def printCommunities(x):
    comunities = []
    nr = net['noNodes']
    for index in range(0, nr+1):
        comunities.append([])
        
    for index in range(0,nr):
        comunities[x[index]].append(index + 1)

    # o populatie are o lista de cromozomi si fiecare cromozom o lista de gene
    #Ex: [1,4,3,1,5,3] 
    #6 gene: [[1,4][][3,6][][5][]]
    #Rezultat dupa eliminare: [[1,4][3,6][5]]

    #elimin listele vide 
    index = 0
    while index < len(comunities):
        if comunities[index] == []:
            comunities.pop(index)
        else:
            index += 1
    return comunities

def afisare_graf(network):
    #lab03/communityDetection/communityGAlive.ipynb: In [4]
    warnings.simplefilter('ignore')
    A=np.matrix(network["mat"])
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size=150, cmap=plt.cm.RdYlBu)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()

def afisare_comunitati(network,bestChromo):
    #lab03/communityDetection/communityGAlive.ipynb: In [5]
    A=np.matrix(network["mat"])
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size = 150, cmap = plt.cm.RdYlBu, node_color = bestChromo.repres)
    nx.draw_networkx_edges(G, pos, alpha = 0.3)
    plt.show()

def main():
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    for g in range(1,gaParam['noGen']+1):
        ga.oneGeneration()      #se constriueste o noua populatie de cromozomi
        
        theBest = ga.bestChromosome()
        print('Generation ' + str(g) + ' : f(x) = ' + str(theBest.fitness) + ' Number of communities:' + str(len(printCommunities(theBest.repres))))

    print('The best solution in generation ' + str(g) + ' is: \n' + str(printCommunities(theBest.repres)))

    #afisare_graf(gaParam["network"])
    afisare_comunitati(gaParam["network"],theBest)
      
main()
