from math import exp
from numpy.linalg import inv
import numpy as np

#https://github.com/lauradiosan/AI-UBB/blob/main/2020-2021/labs/lab09/LogisticRegression.py

def sigmoid(x):
    return 1 / (1 + exp(-x)) #da o valoare reala intre 0 si 1 - valoarea data de discriminator transformata in [0,1]
    
class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    # use the gradient descent method
    # simple stochastic GD
    def fit(self, x, y, learningRate = 0.001, noEpochs = 1000):

        self.coef_ = [0.0 for _ in range(1 + len(x[0]))]    #beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        
        for epoch in range(noEpochs):
            # TBA: shuffle the trainind examples in order to prevent cycles
            for i in range(len(x)): # for each sample from the training data
                ycomputed = sigmoid(self.eval(x[i], self.coef_))     # estimate the output
                crtError = ycomputed - y[i]     # compute the error for the current sample
                for j in range(0, len(x[0])):   # update the coefficients
                    self.coef_[j + 1] = self.coef_[j + 1] - learningRate * crtError * x[i][j]
                self.coef_[0] = self.coef_[0] - learningRate * crtError * 1

        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
 
    def eval(self, xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predictOneSample(self, sampleFeatures):
        coefficients = [self.intercept_] + [c for c in self.coef_]
        return sigmoid(self.eval(sampleFeatures, coefficients))

    def predict(self, inTest):
        computedLabels = [self.predictOneSample(sample) for sample in inTest]
        return computedLabels

    def error(self, computedTestOutputs, testOutputs):
        error = 0.0
        for t1, t2 in zip(computedTestOutputs, testOutputs):
            if t1 != t2:
                error += 1
        error = error / len(testOutputs)

        return error