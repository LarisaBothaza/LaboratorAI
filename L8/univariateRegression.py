from loadData import *
from myBatchGD import *
from splitData import * 

from sklearn.metrics import mean_squared_error
from sklearn import linear_model

NO_EPOCHS = 1000
ALPHA = 0.01

def univariateRegression():

    feature = 'Economy..GDP.per.Capita.'

    #load data from file
    inputs, outputs = loadData("2017.csv", feature, 'Happiness.Score')

    #split data into training data and test data
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)

    #MY BATCH GD
    # initialisation
    myRegressor = myBatchClass(len(trainInputs), NO_EPOCHS, ALPHA) #noEpoch = 1000, alpha/learningRate = 0.01
    # training step
    xx = [[el] for el in trainInputs]
    myRegressor.trainSimple(xx, trainOutputs)
    # save the model parameters
    w0, w1 = myRegressor.intercept, myRegressor.coef[0]
    
    print('The learnt model (manual): f(x) = ', w0, ' + ', w1, '* x1')

    #makes predictions for test data
    computedTestOutputs = myRegressor.predict([[x] for x in testInputs])

    #compute the differences between the predictions and real outputs
    myError = myRegressor.error(testOutputs, computedTestOutputs)
    print("prediction error (manual): ", myError)


def univariateRegressionTOOL():

    feature = 'Economy..GDP.per.Capita.'

    #load data from file
    inputs, outputs = loadData("2017.csv", feature, 'Happiness.Score')

    #split data into training data and test data
    trainInputs, trainOutputs, testInputs, testOutputs = splitDataTool(inputs, outputs)

    # TOOL using sklearn 
    # model initialisation
    regressorTool = linear_model.SGDRegressor(alpha = ALPHA, max_iter = NO_EPOCHS) #alpha = learning_rate

    # training step
    xx = [[el] for el in trainInputs]

    for ep in range(NO_EPOCHS):
        regressorTool.partial_fit(xx, trainOutputs)

    # save the model parameters
    w0t, w1t = regressorTool.intercept_[0], regressorTool.coef_[0]
    print('The learnt model (tool): f(x) = ', w0t, ' + ', w1t, '* x1')

    #makes predictions for test data
    computedTestOutputs = regressorTool.predict([[x] for x in testInputs])

    #compute the differences between the predictions and real outputs
    error = mean_squared_error(testOutputs, computedTestOutputs)
   


def main():
    univariateRegression()
    univariateRegressionTOOL()

main()