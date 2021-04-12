import matplotlib.pyplot as plt 

def plotDataHistogram(x, variableName):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

# plotDataHistogram(inputs[0], 'Economy GDP/Capita')
# plotDataHistogram(inputs[1], 'freedom')
# plotDataHistogram(outputs, 'Happiness score')

##################################################################################
#afisare toate datele: 2D 
# plt.plot(inputs, outputs, 'ro') 
# plt.xlabel('GDP capita')
# plt.ylabel('happiness')
# plt.title('GDP capita vs. happiness')
# plt.show()

def plot3D(inputs, outputs):
    #afisare toate datele: plan 3D
    ax = plt.axes(projection='3d')
    ax.scatter3D(inputs[0], inputs[1], outputs, c=outputs, cmap='Purples')
    plt.title('GDP capita & freedom VS happiness')
    plt.xlabel('GDP capita')
    plt.ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.show()
#plot3D(inputs,outputs)
#####################################################################################

def plot3DTrainAndValidation(trainInputs,trainOutputs,validationInputs,validationOutputs):
    ax = plt.axes(projection='3d')
    ax.scatter(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='Oranges', label="Training data")
    ax.scatter(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Greens', label="Validation data")
    
    plt.xlabel('GDP capita')
    plt.ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.legend()
    plt.title('Train and Validation data')
    plt.show()

def plot3DTrainAndLearnt(xref,yref,zref,trainInputs,trainOutputs):
    ax = plt.axes(projection='3d')
    ax.scatter(xref, yref, zref, c=zref, cmap='winter', label="Learnt model")
    ax.scatter(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='autumn', label="Training data")
    
    plt.xlabel('GDP capita')
    plt.ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.legend()
    plt.title('Train data AND The learnt model')
    plt.show()

def plot3DPredictionsVSRealData(validationInputs,computedValidationOutputs,validationOutputs):
    ax = plt.axes(projection='3d')
    ax.scatter(validationInputs[0], validationInputs[1], computedValidationOutputs, c=computedValidationOutputs, cmap='Blues', label="Computed data")
    ax.scatter(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Reds', label="Real test data")
    
    plt.xlabel('GDP capita')
    plt.ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.legend()
    plt.title('Computed validation (predictions) VS real validation data')
    plt.show()