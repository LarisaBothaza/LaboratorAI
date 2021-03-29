from Ant import Ant

class ACO:
    def __init__(self, acoParams = None, problemParams = None):
        self.acoParams = acoParams
        self.problemParams = problemParams
        self.population = []

    def initialisation(self):
        self.population = []
   
        for _ in range(self.acoParams['colSize']):
            ant = Ant(self.problemParams, self.acoParams)
            self.population.append(ant)

    def oneStepAnt(self): #fiecare furnica face o mutare
        for ant in self.population:
            ant.next()

    def goHomeAnts(self): # se asigura ciclicitatea
        for ant in self.population:
            ant.goHome()

    def updateFeromons(self): # Se modifică urma de feromon de pe drumurile parcurse de toate furnicile (AS)
        # pentru fiecare oras actualizam feromonul (tinand cont si de drumul furnicilor si de evaporare)
        #curs pag 40 
        nodes = self.problemParams['noNodes']

        for i in range(nodes):
            for j in range(nodes):

                deltaFeromon = 0 #Se calculează cantitatea totală de feromoni de pe muchia (ij) 
                for ant in self.population:          
                    if ant.feromonsStatus[i][j] == 1: # dacă furnica a folosit muchia (i,j)
                        deltaFeromon += 1 / ant.cost 
                         # cantitatea de feromon lasata de o furnica (1) / costul turului facut de furnica curenta

                #Se calculează intensitatea urmei de feromoni ca sumă între evaporarea feromonilor vechi şi feromonul nou lăsat
                self.problemParams['feromons'][i][j] = (1 - self.acoParams['evaporation']) * self.problemParams['feromons'][i][j] + deltaFeromon


    def bestAnt(self):
        best = self.population[0]
        for ant in self.population:
            if ant.cost < best.cost: #furnica care a parcurs drumul cel mai scurt
                best = ant
        return best
