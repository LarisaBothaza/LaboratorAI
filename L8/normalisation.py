from sklearn.preprocessing import StandardScaler
from math import sqrt

def normalisationTool(trainData, testData):
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        #encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]
        
        scaler.fit(trainData)  #  fit only on training data
        normalisedTrainData = scaler.transform(trainData) # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
        
        #decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData)  #  fit only on training data
        normalisedTrainData = scaler.transform(trainData) # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

    return normalisedTrainData, normalisedTestData

# statistical normalisation (centered around meand and standardisation)
def statisticalNormalisation(train, test): #In [14]: https://github.com/lauradiosan/AI-UBB/blob/main/2020-2021/labs/lab08/dataNormalisation/dataNormalisation.ipynb
    #mean = average of some numerical data
    meanValue = sum(train) / len(train)
    #stdDev = standard deviation to the mean of some data
    stdDevValue = (1 / len(train) * sum([(feat - meanValue) ** 2 for feat in train])) ** 0.5

    normalisedTrain = [(feat - meanValue) / stdDevValue for feat in train]
    normalisedTest = [(feat - meanValue) / stdDevValue for feat in test]

    return normalisedTrain, normalisedTest

# extract a particular feature (column)
def extractFeature(allData, names, featureName):
    pos = names.index(featureName)
    return [float(data[pos]) for data in allData]

def normalizeInputs(train, test, featureNames):
    normalizedTrainInputs = [[] for _ in range(len(train))]
    normalizedTestInputs = [[] for _ in range(len(test))]

    for index in range(len(featureNames)):
        trainFeature = extractFeature(train, featureNames, featureNames[index])
        testFeature = extractFeature(test, featureNames, featureNames[index])

        normalisedTrainFeature, normalisedTestFeature = statisticalNormalisation(trainFeature, testFeature)

        i = 0
        while (i < len(normalisedTrainFeature)):
            normalizedTrainInputs[i].append(normalisedTrainFeature[i])
            i += 1

        j = 0
        while (j < len(normalisedTestFeature)):
            normalizedTestInputs[j].append(normalisedTestFeature[j])
            j += 1

    return normalizedTrainInputs, normalizedTestInputs