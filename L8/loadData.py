import warnings; warnings.simplefilter('ignore')
import csv
import os

# Linear regression is a linear model, e.g. a model that assumes a linear relationship between the input variables (x) and the single output variable (y). More specifically, that output variable (y) can be calculated from a linear combination of the input variables (x).

# Univariate Linear Regression is a linear regression that has only one input parameter and one output label.

# consider the following regression problem:
# estimate how happiness is influenced by gross domestic product (GDP) per capita. Use 2017 data from ![here](https://www.kaggle.com/unsdsn/world-happiness#2017.csv) 

# load data and consider a single feature (Economy..GDP.per.capita) and the output to be estimated (happiness)

def loadData(fileName, inputVariabName, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1

    selectedVariable = dataNames.index(inputVariabName)
    inputs = [float(data[i][selectedVariable]) for i in range(len(data))]

    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

#verification:
# crtDir =  os.getcwd()
# inputs, outputs = loadData('2017.csv', 'Economy..GDP.per.Capita.', 'Happiness.Score')
# print('in:  ', inputs[:5])
# print('out: ', outputs[:5])

def loadDataMoreInputs(fileName, inputVariabNames, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1

    selectedVariable1 = dataNames.index(inputVariabNames[0])
    selectedVariable2 = dataNames.index(inputVariabNames[1])
    inputs = [[float(data[i][selectedVariable1]), float(data[i][selectedVariable2])] for i in range(len(data))]

    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

#verification:
# crtDir =  os.getcwd()
# inputs, outputs = loadDataMoreInputs("2017.csv", ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')
# print('in:  ', inputs[:5])
# print('out: ', outputs[:5])