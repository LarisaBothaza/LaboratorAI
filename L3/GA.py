from random import randint
from Chromosome import Chromosome

#luat din lab03.fcOptimisation/fcOptimisationGA: In [5]
class GA: #genetic algorithm
    def __init__(self, param=None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = [] #tine minte solutiile potentiale

    @property
    def population(self): #generam populatia
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']): # ma joc cu populatia
            c = Chromosome(self.__problParam)    #se genereaza
            self.__population.append(c)         #se adauga

    def evaluation(self): #calculeaza fitnessul pentru fiecare cromozom
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres,self.__param["network"])

    def bestChromosome(self): #cea mai buna solutie din populatie | cromozul cu fitnesul cel mai mare din generatie
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def worstChromosome(self): #cea mai rea solutie din populatie
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):# procedeu de selectie, iau 2 solutii avute in populatie, la intamplare si o aleg pe cea mai buna
                        # prin intermediul fitnessului
        pos1 = randint(0, self.__param["popSize"] - 1)
        pos2 = randint(0, self.__param["popSize"] - 1)
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self): 
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()       #atribuiesc fitnessul
