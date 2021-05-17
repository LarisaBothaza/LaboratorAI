import numpy as np
from PIL import Image

def loadData():
    inputsPhotos = []
    outputs = []

    with open("fileImgs") as data: 
        lines = data.read()

    for line in lines.splitlines(): 
        image = Image.open("images\\"+ line).resize((200,200))
        arrayImage = np.array(image).flatten()
        inputsPhotos.append(arrayImage)   

        if line.startswith("normal"): 
            outputs.append(1)
        else:
            if line.startswith("sepia"): 
                outputs.append(0)

    #fiecare poza -> o singura lista
    inputs = []
    for array in inputsPhotos:
        arr = []
        for elem in array:
            arr.append(elem)
        inputs.append(arr)

    outputsNames=["sepia", "normal"]

    return inputs, outputs, outputsNames
    
