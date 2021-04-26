from loadData import *
from spliData import *
from myLogisticRegression import *
from normalisation import *
from sklearn.metrics import accuracy_score
from sklearn import linear_model

def accuracy(realLabels, computedLabels):
    return sum([1 if realLabels[i] == computedLabels[i] else 0 for i in range(len(realLabels))])/len(realLabels)

def resolveTool(trainInputsT, trainOutputsT, testInputsT, testOutputsT):

    #step3: normalizare
    trainInputsNT, testInputsNT = normalisationTool(trainInputsT, testInputsT) 

    #step4: invatare model
    linearModelTool = linear_model.LogisticRegression(max_iter=1000)
    linearModelTool.fit(trainInputsNT, trainOutputsT)

    #step5: testare model, forma outputului si interpretarea lui
    w0S, w1S, w2S, w3S, w4S = linearModelTool.intercept_[0], linearModelTool.coef_[0][0], linearModelTool.coef_[0][1], linearModelTool.coef_[0][2], linearModelTool.coef_[0][3]
    print('model SETOSA: y(feat1, feat2, feat3, feat4) = ', w0S, ' + ', w1S, ' * feat1 + ', w2S, ' * feat2 + ',w3S, ' * feat3 +',w4S, ' * feat4')
   
    w0VC, w1VC, w2VC, w3VC, w4VC = linearModelTool.intercept_[1], linearModelTool.coef_[1][0], linearModelTool.coef_[1][1], linearModelTool.coef_[1][2], linearModelTool.coef_[1][3]
    print('model VERSICOLOUR: y(feat1, feat2, feat3, feat4) = ', w0VC, ' + ', w1VC, ' * feat1 + ', w2VC, ' * feat2 + ',w3VC, ' * feat3 +',w4VC, ' * feat4')

    w0V, w1V, w2V, w3V, w4V = linearModelTool.intercept_[2], linearModelTool.coef_[2][0], linearModelTool.coef_[2][1], linearModelTool.coef_[2][2], linearModelTool.coef_[2][3]
    print('model VIRGINICA: y(feat1, feat2, feat3, feat4) = ', w0V, ' + ', w1V, ' * feat1 + ', w2V, ' * feat2 + ',w3V, ' * feat3 +',w4V, ' * feat4')

    skpred = linearModelTool.predict(testInputsNT)

    print('Sklearn outputs: ', skpred)
    print('Real outputs:    ', testOutputsT)

    error = 1 - accuracy_score(testOutputsT, skpred)
    print("Classification error (tool): ", error)

    #step6: calcul metrici de performanta (acc)
    print("Tool Accuracy: ", accuracy(testOutputsT, skpred)) 

    return skpred, testOutputsT

def resolveMyCode(trainInputs, trainOutputs, testInputs, testOutputs):

    #print("inainte"), print(trainInputs)

    #step3: normalizare
    trainInputs, testInputs = normalizeInputs(trainInputs, testInputs) #manual normalisation

    #print("dupa"), print(trainInputs)

    #step4: invatare model - implementare proprie 
    classifier = MyLogisticRegression()

    computedTestO = []
    for i in range(3):
        trainO = [1 if x == i else 0 for x in trainOutputs] #1 daca e clasa respectiva, 0 pentru restul
        classifier.fit(trainInputs, trainO)
        computedTestO.append(classifier.predict(testInputs)) #facem predicitii pentru fiecare

        w0, w1, w2, w3, w4 = classifier.intercept_, classifier.coef_[0], classifier.coef_[1], classifier.coef_[2], classifier.coef_[3]
        if(i == 0):
            print("SETOSA", end=" ")
        else:
            if (i == 1):
                print("VERSICOLOUR", end=" ")
            else:
                if (i == 2):
                    print("VIRGINICA", end=" ")
        print('model: y(feat1, feat2, feat3, feat4) = ', w0, ' + ', w1, ' * feat1 + ', w2, ' * feat2 + ',w3, ' * feat3 +',w4, '* feat4')
        
    
    #identificarea celei mai mari valori din computed - pozitia valorii maximale indica eticheta corecta asociata
    computedTestOutputs = []
    for i in range(len(computedTestO[0])):
        values = [computedTestO[0][i], computedTestO[1][i], computedTestO[2][i]]
        computedTestOutputs.append(values.index(max(values))) #pune eticheta cu valoarea probabilitatii cea mai mare

    #step5: testare model, forma outputului si interpretarea lui
    print('Computed outputs:', computedTestOutputs)
    print('Real outputs:    ', testOutputs)

    error = classifier.error(computedTestOutputs, testOutputs)
    print("Classification error (manual): ", error)

    error = 1 - accuracy_score(testOutputs, computedTestOutputs)
    print("Classification error (tool): ", error)

    #step6: calcul metrici de performanta (acc)
    print("Manual Accuracy: ", accuracy(testOutputs, computedTestOutputs))

    return computedTestOutputs
    
def transform(vector):
    arr = []
    for i in vector:
        if i == 0:
            arr.append("Iris setosa         ")
        else:
            if i == 1:
                arr.append("Iris versicolor     ")
            else:
                if i == 2:
                    arr.append("Iris virginica      ")
    return arr

def main():

    #step1: load data (4 features)
    inputs, outputs = readData()

    #step2: impartire pe train si test
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)

    print("----------------------------------------------My logistic regression--------------------------------------------------------")
    computedTestOutputs = resolveMyCode(trainInputs, trainOutputs, testInputs, testOutputs)
    print("\n----------------------------------------------Tool logistic regression------------------------------------------------------")
    skpred, testOutputs = resolveTool(trainInputs, trainOutputs, testInputs, testOutputs)

    realString = transform(testOutputs)
    computedString = transform(computedTestOutputs)
    sklearnString = transform(skpred)

    print("\n")
    print("REAL                  COMPUTED             SKLEARN")
    for i in range(len(skpred)):
        print("___________________________________________________________")
        print(realString[i], computedString[i], sklearnString[i])
    print("\n")    

main()
  

