from random import random
# Batch GD
# Eroarea se calculează pentru fiecare exemplu de antrenament
# Modelul se updatează dupa ce toate exemplele de antrenament au fost evaluate (la finalul unei epoci)

class myBatchClass:
    def __init__(self, length, noEpochs, learningRate):
        self.length = length 
        self.noEpochs = noEpochs
        self.learningRate = learningRate
        self.coef = [0.0 for _ in range(self.length)]
        self.intercept = random()

    def train(self, x, y):
        #formule: curs 5, pagina 13

        for epoch in range(self.noEpochs):
            error_coef = 0.0
            error_intercept=0.0

            for i in range(len(x)):    # for each sample from the training data
                ycomputed = self.eval(x[i])     # estimate the output
                crtError = ycomputed - y[i]     # compute the error for the current sample
                
                for j in range(len(x[0])):
                    error_coef = error_coef + crtError * x[i][j]
                    error_intercept = error_intercept + crtError

            #update the coefficients
            for j in range(len(x[0])):
                self.coef[j] = self.coef[j] - self.learningRate * (error_coef / len(x))

            self.intercept = self.intercept - self.learningRate * (error_intercept / len(x))

    def trainSimple(self, x, y):
        #formule: curs 5, pagina 13

        for epoch in range(self.noEpochs):
            error_coef = 0.0
            error_intercept=0.0

            for i in range(len(x)):    # for each sample from the training data
                ycomputed = self.eval(x[i])     # estimate the output
                crtError = ycomputed - y[i]     # compute the error for the current sample
                
                for j in range(len(x[0])):
                    error_coef = error_coef + crtError * x[i][j]
                    
            #update the coefficients
            for j in range(len(x[0])):
                self.coef[j] = self.coef[j] - self.learningRate * (error_coef / len(x))

            self.intercept = self.intercept - self.learningRate * crtError


    def eval(self, xi):
        yi = self.coef[-1]

        for j in range(len(xi)):
            yi += self.coef[j] * xi[j]
        return yi

    def predict(self, x):
        yComputed = [self.eval(xi) for xi in x]
        return yComputed

    def error(self, real, computed):
       error = 0.0
       for y1, y2 in zip(computed, real):
           error += (y1-y2) ** 2
       error = error / len(computed)
       return error