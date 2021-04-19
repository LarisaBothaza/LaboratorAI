import numpy as np
import random 

# Split the Data Into Training and Test Subsets
# In this step we will split our dataset into training and testing subsets (in proportion 80/20%).

# Training data set is used for training the linear model. Testing dataset is used for validating of the model. All data from testing dataset will be new to  model and we may check how accurate are model predictions.

def splitData(inputs, outputs):
     # split data into training data (80%) and testing data (20%)
    np.random.seed(5)
    
    indexes = [i for i in range(len(inputs))]

     #trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace = False)
    trainSample = []

    for i in range(0, int(0.8*len(inputs))+1):
         nr = random.randint(0,(len(inputs)-1))
         if not (trainSample.__contains__(nr)):
              trainSample.append(nr)

    testSample = [i for i in indexes  if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    return trainInputs, trainOutputs, testInputs, testOutputs


def splitDataTool(inputs, outputs):
     # split data into training data (80%) and testing data (20%)
    np.random.seed(5)
    
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace = False)

    testSample = [i for i in indexes  if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    return trainInputs, trainOutputs, testInputs, testOutputs
