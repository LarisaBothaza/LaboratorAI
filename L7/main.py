
from loadData import *
from splitData import *
from plots import *
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def training(trainInputs,trainOutputs):
    # training step
    # training the model by using the training inputs and known training outputs
    xx = [[el1,el2] for el1,el2 in zip(trainInputs[0],trainInputs[1])]

    # regressor = linear_model.SGDRegressor(max_iter =  10000)
    regressor = linear_model.LinearRegression()
    regressor.fit(xx, trainOutputs)

    # save the model parameters
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    print('The learnt model: f(x) = ', w0, ' + ', w1, '*x1', ' + ', w2, '*x2')

    return w0, w1, w2

def syntheticData(trainInputs,noOfPoints):
    #prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
    ref = []
    val = min(trainInputs)
    step = (max(trainInputs) - min(trainInputs)) / noOfPoints
    for i in range(1, noOfPoints):
        ref.append(val)
        val += step
    return ref

def main():
    # put all steps togheter
    # using sklearn 

    # loadData
    crtDir =  os.getcwd()
    filePath = os.path.join(crtDir, '2017.csv')
    inputs, outputs = loadData(filePath, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')

    #show plots: show data, check the linearity
    plotDataHistogram(inputs[0], 'Economy GDP/Capita')
    plotDataHistogram(inputs[1], 'Freedom')
    plotDataHistogram(outputs, 'Happiness score')
    plot3D(inputs, outputs)

    #split the data in training data (80%) and validation/test data (20%)
    trainInputs, trainOutputs, validationInputs, validationOutputs = splitData(inputs, outputs)

    #plot the train and validation data
    plot3DTrainAndValidation(trainInputs, trainOutputs, validationInputs, validationOutputs)

    #learning step
    w0, w1, w2 = training(trainInputs, trainOutputs)
    
    #plot the learnt model
    #prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
    noOfPoints = 800

    xref = syntheticData(trainInputs[0], noOfPoints)
    yref = syntheticData(trainInputs[1], noOfPoints)

    zref = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(xref,yref)]

    #plot train data and the learnt model
    plot3DTrainAndLearnt(xref, yref, zref, trainInputs, trainOutputs)

    #makes predictions for test data
    # use the trained model to predict new inputs
    computedValidationOutputs  = [w0+w1*el1+w2*el2 for el1,el2 in zip(validationInputs[0], validationInputs[1])]

    # plot the computed outputs (see how far they are from the real outputs)
    plot3DPredictionsVSRealData(validationInputs, computedValidationOutputs, validationOutputs)

    #compute the differences between the predictions and real outputs
    error = mean_squared_error(validationOutputs, computedValidationOutputs)
    print('Prediction error (tool): ', error)

main()