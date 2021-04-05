
import matplotlib.pyplot as plt

def grafic(realOutputs,computedOutputs):
    # plot the data
    indexes = [i for i in range(len(realOutputs))]
    real, = plt.plot(indexes, realOutputs, 'ro', label = 'real')
    computed, = plt.plot(indexes, computedOutputs, 'bo', label = 'computed')
    plt.xlim(0,8)
    plt.ylim(0, 10)
    plt.legend([real, (real, computed)], ["Real", "Computed"])
    plt.show()


def evalClassification(realOutputs, computedOutputs, pos):
    TP = sum([1 if (realOutputs[i] == pos and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    FP = sum([1 if (realOutputs[i] != pos and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    TN = sum([1 if (realOutputs[i] != pos and computedOutputs[i] != pos) else 0 for i in range(len(realOutputs))])
    FN = sum([1 if (realOutputs[i] == pos and computedOutputs[i] != pos) else 0 for i in range(len(realOutputs))])

    #precision indicates how accurate the positive predictions are:
    precision = TP / (TP + FP)
    #recall indicates the coverage of actual positive sample
    recall = TP / (TP + FN)

    return precision, recall

def eval(realLabels, computedLabels, labels):
    precision = []
    recall = []
    for label in labels:
        p, r = evalClassification(realLabels, computedLabels, label)
        precision.append(p)
        recall.append(r)
    return precision, recall

#CLASIFICARE
#multiclass  - TEMA 2
def multiClass():
    labels = ["basket", "football", "handball"]

    realLabels = ["basket", "football", "football", "football", "handball", "basket", "handball","handball"]
    #computedLabels = ["basket", "football", "handball", "football", "handball", "basket", "handball", "handball"]
    computedLabels = ["football", "football", "basket", "football", "basket", "handball", "handball", "handball"]

    precision, recall = eval(realLabels, computedLabels, labels)
    acc = sum([1 if realLabels[i] == computedLabels[i] else 0 for i in range(0, len(realLabels))]) / len(realLabels)
    print("Accuracy: " + str(acc) + " Precision: " + str(precision) + " Recall: " + str(recall))
    #grafic(realLabels,computedLabels)

multiClass()

#Precizia = TP / TP+FP
#Rapel = TP / TP + FN
#Acuratete = Nr de exemple corect clasificate / nr total de exemple (Clasa pozitiva)