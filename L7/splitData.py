import numpy as np 
import matplotlib.pyplot as plt 

# Split the Data Into Training and Test Subsets
# In this step we will split our dataset into training and testing subsets (in proportion 80/20%).

# Training data set is used for learning the linear model. 
# Testing dataset is used for validating of the model. 
# All data from testing dataset will be new to model and we may check how accurate are model predictions.

def splitData(inputs, outputs): #inputs with 2 values and 1 outputs
    np.random.seed(5)
    length = len(outputs)
    indexes = [i for i in range(length)]

    trainSample = np.random.choice(indexes, int(0.8 * length), replace = False)
    validationSample = [i for i in indexes  if not i in trainSample]

    trainInputs1 = []
    trainInputs2 = []

    for i in trainSample:
        trainInputs1.append(inputs[0][i])
        trainInputs2.append(inputs[1][i])

    trainInputs = [trainInputs1,trainInputs2]
    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs1 = []
    validationInputs2 = []

    for i in validationSample:
        validationInputs1.append(inputs[0][i])
        validationInputs2.append(inputs[1][i])

    validationInputs = [validationInputs1,validationInputs2]
    validationOutputs = [outputs[i] for i in validationSample]

    return trainInputs, trainOutputs, validationInputs, validationOutputs