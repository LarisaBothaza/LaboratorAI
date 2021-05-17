def training(classifier, trainInputs, trainOutputs):
    # step4: training the classifier
    # identify (by training) the classification model
    classifier.fit(trainInputs, trainOutputs)

def classification(classifier, testInputs):
    # step5: testing (predict the labels for new inputs)
    # makes predictions for test data 
    computedTestOutputs = classifier.predict(testInputs)

    return computedTestOutputs

def evalMultiClass(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix

    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])

    return acc, precision, recall