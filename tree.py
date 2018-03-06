from numpy import *
import operator
def createTree(dataset,labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featureValues = [example[bestFeat] for example in dataset]
    uniqueVals =set(featureValues)
    for values in uniqueVals:
        sublabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitdataset(dataset,bestFeat,value),sublabels)
    return myTree
import matplotlib.pyplot as plt
decision = dict(boxstyle = 'sawtooth',fc ='0.8')
leafNode = dict(boxstyle= "round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,
                            textcoords='axes fraction',
                            va='center',
                            ha='center',
                            bbox=nodeType,
                            arrowprops=arrow_args)
def createPlot(inTree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])

    createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getNumleafs(inTree))
    plotTree.totlaD = float(getTreeDepth(inTree))
    plotTree.xoff = -0.5/plotTree.totalW;plotTree.yoff = 1.0
    plotTree(inTree,(0.5,1.0),'')
    plot.show()
def getNumleafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()
    seconddict = firstStr.keys()[0]
    for key in seconddict.keys():
        if type(seconddict[key]).__name__ == 'dict':
            numLeafs += getNumleafs(seconddict[key])
        else:
            numLeafs += 1
    return numLeafs
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    seconddeict = myTree[firstStr]
    for key in seconddeict.keys():
        if type(seconddeict[key]).__name__ == 'dict':
            thisDepth = 1+getDepth(seconddeict[key])
        else:
            thisDepth = 1
    if thisDepth >maxDepth:
        maxDepth = thisDepth
    return maxDepth
def plotMidText(cntPt, parentPt, txtString):
    xMid = (parentPt[0]-cntPt[0])/2.0+cntPt[0]
    yMid = (parentPt[1]-cntPt[1])/2.0+cntPt[1]
    createPlot().ax1.text(xMid,yMid,txtString)
def plotTree(myTree,parentPt,nodeTxt):
    numLeafs = getNumleafs(myTree)
    depth = getTreeDepth(myTree)
    firststr = list(myTree.keys())[0]
    cntrPt = (plotTree.xoff + float(numLeafs)/2.0/plotTree.totalW,plotTree.yoff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firststr,cntrPt,parentPt,nodeTxt)
    secondDict = myTree[firstStr]
    plotTree.yoff = plotTree.yoff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[keys]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xoff = plotTree.xoff +1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xoff,plotTree.yoff),cntrPt,leafNode)
            plotMidText((plotTree.xoff,plotTree.yoff),cntrPt,str(key))
    plotTree.yoff = plotTree.yoff + 1.0/plotTree.totalD

def classify(inputTree,featLabels,testVect):
    firstStr = inputTree.keys()[0]
    seconddict = inputTree[firstStr]
    featIndex = featLabels,index(firstStr)
    for key in seconddict.keys():
        if testVect[featIndex] == key:
            if type(seconddict[key]).__name__ == 'dict':
                classLabel = classify(seconddict[key],featLabels,testVect)
            else:
                classLabel = seconddict[key]
    return classLabel

fr = open('lense.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lenseLabel = ['age','prescript','astigmatic','tearRate']
lenseTree = tree.createTree(lenses,lenseLabel)