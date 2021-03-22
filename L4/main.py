from GA import GA
from Chromosome import Chromosome
from utils import *


def pseudoTestXO():
    # seed(5)
    problParam = {'noNodes' : 10}
    c1 = Chromosome(problParam)
    c2 = Chromosome(problParam)
    print('parent1: ', c1)
    print('parent2: ', c2)
    off = c1.crossover(c2)
    print('offspring: ', off)

#pseudoTestXO()

# parent1:  
# Chromo: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] has fit: 0.0
# parent2:  
# Chromo: [0, 1, 2, 9, 4, 5, 6, 7, 8, 3] has fit: 0.0
# offspring:  
# Chromo: [6, 7, 8, 3, 0, 1, 2, 9, 4, 5] has fit: 0.0

def pseudoTestMutation():
    problParam = {'noNodes' : 10}
    c1 = Chromosome(problParam)
    print('before mutation: ', c1)
    c1.mutation()
    print('after mutation: ', c1)

#pseudoTestMutation()

# before mutation:  
# Chromo: [0, 1, 2, 8, 4, 5, 6, 7, 3, 9] has fit: 0.0
# after mutation:  
# Chromo: [0, 1, 2, 8, 4, 5, 3, 6, 7, 9] has fit: 0.0

nrNoduri,mat = readFromFileHard('hard_01_tsp.txt')

gaParam = {"popSize": 600, "noGen": 400, "network": mat}

problParam = {'function': fitness, 'retea': mat,'noNodes':nrNoduri}


def main():
    #seed = 10
    ga = GA(gaParam, problParam)
    ga.initialisation() # fac o initializare, generez noGen de cromozomi si ii adaug in populatie
    ga.evaluation()   # evaluez fitness-ul, sa vad cat de buni sunt cu functia fitness

    for g in range(gaParam['noGen']):

        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()

        reprez = []
        for r in bestChromo.repres:
            reprez.append(r+1)

        print(str(bestChromo.fitness) + ' --- ' + str(reprez))
        
main()

      

