
# load data and consider two features (Economy..GDP.per.capita, Freedom) and the output to be estimated (happiness)
import csv
import os

def loadData(fileName, inputVariabName, outputVariabName): #din LIVEdoc 
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

    #selectedVariable = dataNames.index(inputVariabName)  #for SINGLE
    selectedVariables=[]
    for var in inputVariabName:
        selectedVariables.append(dataNames.index(var))

    #inputs = [float(data[i][selectedVariable]) for i in range(len(data))]  #for SINGLE

    inputs = []
    
    for j in range(len(selectedVariables)):
        auxInput = []
        for i in range(len(data)):
            auxInput.append(float(data[i][selectedVariables[j]]))

        inputs.append(auxInput)

    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

# crtDir =  os.getcwd()
# filePath = os.path.join(crtDir, '2017.csv')

# inputs, outputs = loadData(filePath, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')
# print('in:  ', inputs[:5])
# print('out: ', outputs[:5])