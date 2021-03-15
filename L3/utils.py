from random import randint
import networkx as nx

def generateNewRandomValue(number1, number2):
    return randint(number1, number2)

#reprezentarea retelei
def representation(ret):
    #label-based representation Pizzuti
    repres = [generateNewRandomValue(0, ret['noNodes'] - 1) for _ in range(ret['noNodes'])]
    #se genereaza un vector cu numere random inte 0 si range(ret), ret = reteaua # NOD = GENA

    return repres
