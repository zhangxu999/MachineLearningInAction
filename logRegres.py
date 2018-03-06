import numpy as np
from numpy import mat,shape,exp,ones
from numpy import *
import pandas as pd
from pandas import DataFrame

def colicTest():
    frTrain = open('Ch05/horseColicTraining.txt')
    frTest = open('Ch05/horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float[currLine[21]])
    trainWeights = stocGrandAscent1(array[trainingSet],trainingLabels,500)
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr)),trainWeights) != currLine[21]:
            errorCount  += 1
    errorRate = float(errorCount)/numTestVec
    print('the errror rate is :%f'%errorRate)
    return errorRate
def multiTest():
    numtest = 10;errorSum = 0
    for k in range(numtest):
        errorSum += colicTest()
        print('after %d iterations the average error rate is: %f :'%(numtest,errorSum/float(numtest)))