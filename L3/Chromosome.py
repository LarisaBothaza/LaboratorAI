from random import randint
from utils import representation, generateNewRandomValue

#un cromozom = solutie candidat
#un cromozom are popSize gene 
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = representation(problParam['retea'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l = []):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit = 0.0):
        self.__fitness = fit

    def crossover(self, c): #incrucisare prin taietura random 
        r = randint(0, len(self.__repres) - 1)      
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self): # se iau 2 gene la intamplare si se interschimba
        pos1 = randint(0, len(self.__repres)-1) 
        pos2 = randint(0, len(self.__repres)-1) 
        aux = self.__repres[pos1]
        self.__repres[pos1] = self.__repres[pos2]
        self.__repres[pos2] = aux

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness