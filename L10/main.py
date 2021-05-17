from loadData import *
from splitData import *
from normalisation import *
from ann_tool import *

def transform(vector):
    arr = []
    for i in vector:
        if i == 0:
            arr.append("sepia          ")
        else:
            if i == 1:
                arr.append("normal         ")

    return arr

def main():
    from sklearn import neural_network

    inputs, outputs, outputName = loadData()

    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs,outputs)
    
    trainInputsNormalised, testInputsNormalised = normalisation(trainInputs, testInputs)

    # non-liniar classifier and softmax approach for multi-class 
    classifier = neural_network.MLPClassifier(hidden_layer_sizes = (5,), activation = 'relu', max_iter = 100, solver = 'sgd', verbose=10, random_state = 1, learning_rate_init = 0.01)

    training(classifier, trainInputsNormalised, trainOutputs)

    predictedLabels = classification(classifier, testInputsNormalised)

    acc, prec, recall = evalMultiClass(np.array(testOutputs), predictedLabels, outputName)
    
    print('precision: ', prec)
    print('recall: ', recall)
    print("\n")
    print('acc: ', acc)

    predictedLabelsString = transform(predictedLabels)
    testOutputsString = transform(testOutputs)

    print("\n")
    print("REAL           COMPUTED")
    for i in range(len(testOutputsString)):
        print("________________________")
        print(testOutputsString[i], predictedLabelsString[i])
    print("\n") 

main()