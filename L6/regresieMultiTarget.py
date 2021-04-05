from math import sqrt

def sumL1(r1, c1):
    suma = 0.0
    for i in range(len(r1)):
                #|(realOutputs-computedOutputs)|
        suma += abs(r1[i] - c1[i])
    return suma

def sumL2(r2, c2):
    suma = 0.0
    for i in range(len(r2)):
                #(realOutputs-computedOutputs)^2
        suma += (r2[i] - c2[i]) ** 2
    return suma

def errors(realOutputs, computedOutputs):
    # MAE                                     
    errorL1 = sum(sumL1(r, c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
    print('Error (MAE - the absolute difference): ', errorL1)
    # RMSE
    errorL2 = sqrt(sum(sumL2(r, c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs))
    print('Error (RMSE - the square difference): ', errorL2)

#REGRESIE
#multi-target - TEMA 1
def multiTarget():
    realOutputs = [[4, 5, 6], [1, 2, 3], [10, 20, 30], [5, 15, 25]]
    computedOutputs = [[5, 7.4, 6.5], [1, 2, 2.8], [10.2, 19, 30.1], [4.9, 15, 25]]
    print('Prediction error:')
    errors(realOutputs, computedOutputs)
    
multiTarget()