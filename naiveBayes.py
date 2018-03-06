def loadDateset():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]
    return postingList
def createVocabList(dataSet):
    vocabSet = set([])
    for doc in dataSet:
        vocabSet = vocabSet|set(doc)
    return list(vocabSet)
def setOfWordsVec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in vocabList:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word %s: not in vocablist"%word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDoc = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbsive = sum(trainCategory) / float(numTrainDoc)
    p0Num = ones(numWords);
    p1Num = ones(numWords)
    p0Denom = 2.0;
    p1Denom = 2.0;
    for i in range(numTrainDoc):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom +=sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
def classifyNB(vec2Classify,p0vec,p1vec,pclass1):
    p1 = sum(vec2Classify*p1vec)+log(pclass1)
    p0 = sum(vec2Classify*p0vec)+log(1.0-pclass1)
    if p1 > p0:
        return 1
    else:
        return 0

def traingNB():
    listOPosts,listClasses = loadDateset()
    myVocablist = createVocabList(listOPosts)
    trainMat = []
    for postdoc in  listOPosts:
        trainMat.append(setOfWordsVec(myVocablist,postdoc))
    p0v,p1v,pAb = traingNB(trainMat,listClasses)
    testEntry = ['love','my','dalmation']
    thisdoc = array(setOfWordsVec(myVocablist,testEntry))
    print(testEntry, "classified as:", classifyNB(thisdoc, p0v, p1v, pAb))
    testEntry = ['stupid','garbage']
    thisdoc = array(setOfWordsVec(myVocablist,testEntry))
    print(testEntry, "classified as:", classifyNB(thisdoc, p0v, p1v, pAb))

