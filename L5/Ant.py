from random import *

class Ant:
    def __init__(self, problemParams = None, acoParams = None ):
        self.acoParams = acoParams
        self.problemParams = problemParams
        self.cost = 0
        self.path = [randint(0, self.problemParams['noNodes'] - 1)] # oraşul din care pleacă în căutare
        #0 = nevizitat, 1 = vizitat - deci a lasat feromon
        self.feromonsStatus = [[0 for _ in range(self.problemParams['noNodes'])] for _ in range(self.problemParams['noNodes'])]

    def next(self): #pag 37 formula (din curs) dupa care se alege urmatorul oras
        # aplha - controlează importanţa urmei (câte furnici au mai trecut pe muchia respectivă)
        # beta - controlează importanţa vizibilităţii (cât de aproape se află următorul oraş)
        alpha = self.acoParams['alpha']
        beta = self.acoParams['beta']
       
        taXnb = []
        sumE = 0.0
        noNodes = self.problemParams['noNodes']

        for indexOras in range(noNodes):
            taXnb.append(0)

            if indexOras not in self.path:
                if self.problemParams['feromons'][self.path[-1]][indexOras] == 0:
                    t = 1
                else:
                        #intensitatea urmei de feromon pe muchia (i,j) 
                    t = pow(self.problemParams['feromons'][self.path[-1]][indexOras], alpha)

                d = self.problemParams['network'][self.path[-1]][indexOras]
                n = pow((1 / d),beta)

                taXnb[-1] = t*n #arg max {} din pag 37
                sumE += taXnb[-1] #adunarea din a doua formula 37

        q = uniform(0, 1)
        q0 = self.acoParams['probQ']  # probabilitatea dupa care se alege orasul cel mai "optim"

        if q < q0 : 
            #arg max{t*n}
            maxx = 0
            maxIndex = 0

            for oras in range(noNodes):
                if taXnb[oras] > maxx:
                    maxx = taXnb[oras] 
                    maxIndex = oras

            nextCity = maxIndex

        else:
            #J - oras ales cu o anume probabilitate, probabilitate calcultata mai jos
            myList = []
            probabilitate = [] #probabilitatea de tranziţie a furnicii k situată în oraşul i spre oraşul j
            for oras in range(noNodes):
                if taXnb[oras] != 0:
                    myList.append(oras)
                    probabilitate.append(taXnb[oras] / sumE)

            nextCity = choices(myList, weights=probabilitate)[0]

        #adaug orasul in traseu, cresc costul si marchez orasulcu feromon
        self.path.append(nextCity)
        self.cost += self.problemParams['network'][self.path[-2]][self.path[-1]] #creste costul 

        self.feromonsStatus[self.path[-2]][self.path[-1]] = 1 #viziteaza muchia 
        self.feromonsStatus[self.path[-1]][self.path[-2]] = 1 #viziteaza muchia 
        

    def goHome(self):
        #se intoarce la primul oras (de unde a plecat)
        self.path.append(self.path[0])
        self.cost += self.problemParams['network'][self.path[-2]][self.path[-1]]
        
