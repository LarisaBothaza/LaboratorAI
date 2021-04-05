
#loss-ul (funcția de cost) în cazul problemelor de clasificare binară 
# (outputul clasificatorului este reprezentat ca o matrice cu $noSamples x2
#  valori reale subunitare; fiecare linie are suma elementelor 1, elementele reprezentand 
# probabilitatile prezise pt fiecare din cele 2 clase)

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, log_loss
#Live 3: in [4]
def evalClassificationV1(realLabels, computedLabels, labelNames):
    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)
    return acc, precision, recall 

def loss1(): #binar
# consider some real labels and, instead of some predicted labels, we have some values (real values representing probabilities asscoaited to our labels) (obtained by the ML algorithm - a classifier)
# we want ot estimate the error of prediction (classification)
# Problem specification:
# input: realLabels, computedOutputs - arrays of the same length containing labels (some discrete values) and real values, respectively
# output: accuracy, precision, recall - real values in range [0,1]

# if the rawOutputs of the ML algorithms are probabilities (not labels)
    realLabels = ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
    computedOutputs = [[0.7, 0.3], [0.2, 0.8], [0.4, 0.6], [0.9, 0.1], [0.7, 0.3], [0.4, 0.6]]
    
    # step1: transform the raw outputs into labels
    #by using NumPy library
    import numpy as np
    labelNames = list(set(realLabels))
    computedLabels = [labelNames[np.argmax(p)] for p in computedOutputs]

    # step2: compute the performance
    acc, prec, recall = evalClassificationV1(realLabels, computedLabels, ['spam', 'ham'])

    print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)
    
    print("loss: ",log_loss(realLabels,computedOutputs) )
   

loss1()


