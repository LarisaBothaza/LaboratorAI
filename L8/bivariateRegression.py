
from loadData import loadDataMoreInputs
from splitData import splitData, splitDataTool
from normalisation import *
from myBatchGD import *

from sklearn import linear_model
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt 

NO_EPOCHS = 1000
ALPHA = 0.01

def plot3Ddata(x1Train, x2Train, yTrain, x1Model = None, x2Model = None, yModel = None, x1Test = None, x2Test = None, yTest = None, title = None):
    from mpl_toolkits import mplot3d
    ax = plt.axes(projection = '3d')
    if (x1Train):
        plt.scatter(x1Train, x2Train, yTrain, c = 'r', marker = 'o', label = 'train data') 
    if (x1Model):
        plt.scatter(x1Model, x2Model, yModel, c = 'b', marker = '_', label = 'learnt model') 
    if (x1Test):
        plt.scatter(x1Test, x2Test, yTest, c = 'g', marker = '^', label = 'test data')  
    plt.title(title)
    ax.set_xlabel("capita")
    ax.set_ylabel("freedom")
    ax.set_zlabel("happiness")
    plt.legend()
    plt.show()

def bivariateRegression():

    features=['Economy..GDP.per.Capita.', 'Freedom']

    #load data from file
    inputs, outputs = loadDataMoreInputs("2017.csv", features, 'Happiness.Score')

    #split data into training data and test data
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)

    #plot BEFORE normalisation
    feature1train = [ex[0] for ex in trainInputs]
    feature2train = [ex[1] for ex in trainInputs]

    feature1test = [ex[0] for ex in testInputs]
    feature2test = [ex[1] for ex in testInputs]
    plot3Ddata(feature1train, feature2train, trainOutputs, [], [], [], feature1test, feature2test, testOutputs, 'capita vs freedom vs happiness')

    # manual data normalisation
    trainInputsNormalisated, testInputsNormalisated = normalizeInputs(trainInputs, testInputs, features)
    trainOutputsNormalisated, testOutputsNormalisated = statisticalNormalisation(trainOutputs, testOutputs)

    #plot AFTER normalisation
    feature1train = [ex[0] for ex in trainInputsNormalisated]
    feature2train = [ex[1] for ex in trainInputsNormalisated]
    trainOutput = [ex for ex in trainOutputsNormalisated]

    feature1test = [ex[0] for ex in testInputsNormalisated]
    feature2test = [ex[1] for ex in testInputsNormalisated]
    testOutput = [ex for ex in testOutputsNormalisated]

    plot3Ddata(feature1train, feature2train, trainOutputs, [], [], [], feature1test, feature2test, testOutputs, "train and test data (after normalisation)")
 
    #MY BATCH GD
    #initialisation
    myBatch = myBatchClass(len(trainInputsNormalisated[0]), NO_EPOCHS, ALPHA)
    # training step
    myBatch.train(trainInputsNormalisated, trainOutputsNormalisated)
    # save the model parameters
    w0, w1, w2 = myBatch.intercept, myBatch.coef[0],  myBatch.coef[1]
    print('The learnt model (manual batch): f(x) = ', w0, ' + ', w1, '*x1', ' + ', w2, '*x2')

    #compute the differences between the predictions and real outputs
    computedTestOutputs = myBatch.predict(testInputsNormalisated)
    err = myBatch.error(testOutputsNormalisated, computedTestOutputs)
  
    print("my error prediction (manual):" + str(err))
    print("error for my regressor (tool): " + str(mean_squared_error(computedTestOutputs, testOutputsNormalisated)))
    


def TOOLbivariateRegression():

    features=['Economy..GDP.per.Capita.', 'Freedom']

    #load data from file
    inputs, outputs = loadDataMoreInputs("2017.csv", features, 'Happiness.Score')

    #split data into training data and test data
    trainInputs, trainOutputs, testInputs, testOutputs = splitDataTool(inputs, outputs)

    # TOOL data normalisation
    trainInputsNormalisated, testInputsNormalisated = normalisationTool(trainInputs, testInputs)
    trainOutputsNormalisated, testOutputsNormalisated = normalisationTool(trainOutputs, testOutputs)

    #TOOL
    # model initialisation
    toolRegressor = linear_model.SGDRegressor(alpha=ALPHA)

    for ep in range(1000):
        toolRegressor.partial_fit(trainInputsNormalisated, trainOutputsNormalisated)

    w0t, w1t, w2t = toolRegressor.intercept_[0], toolRegressor.coef_[0], toolRegressor.coef_[1]
    print('The learnt model (tool): f(x) = ', w0t, ' + ', w1t, '*x1', ' + ', w2t, '*x2')
 
    #compute the differences between the predictions and real outputs
    computedTestOutputs = toolRegressor.predict(testInputsNormalisated)
  
    print("error for tool regressor (tool): " + str(mean_squared_error(computedTestOutputs, testOutputsNormalisated)))

def main():
    TOOLbivariateRegression()
    bivariateRegression()

main()

