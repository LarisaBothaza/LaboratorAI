from sklearn.datasets import load_iris

def readData():
    data = load_iris()
    inputs = data['data']
    outputs = data['target']
    featureNames = list(data['feature_names'])

    inputs = [[feat[featureNames.index('sepal length (cm)')], feat[featureNames.index('sepal width (cm)')],
                feat[featureNames.index('petal length (cm)')], feat[featureNames.index('petal width (cm)')]]
              for feat in inputs]

    return inputs, outputs