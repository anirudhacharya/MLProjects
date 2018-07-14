'''
Created on Mar 11, 2014

@author: Anirudh
'''
"""

"""
import math

def getNearTopics(curPos,topicInfo):
    distance = lambda a,b: math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)
    distTopic = {}
    for i in topicInfo:
        dist = format(distance((i[1],i[2]),curPos), '.3f')
        if dist in distTopic:
            distTopic[dist].append(int(i[0]))
        else:
            distTopic[dist] = [int(i[0])]
    
    topicList = []
    for i in sorted(distTopic.keys()):
        topicList = topicList + sorted(distTopic[i],reverse=True)
    
    return topicList

def getNearQuestions(nearTopics,topicQues):
    nearQues = []
    for i in nearTopics:
        curTopicQues = sorted(topicQues[i], reverse=True)
        for j in curTopicQues:
            if j not in nearQues:
                nearQues.append(j)
    
    return nearQues

if __name__ == "__main__":
    '''fHandle = open('input','r')
    fileInput = fHandle.read()
    fileInput = fileInput.split('\n')'''
    firstLine = raw_input() #fileInput[0].split(' ')
    fileInput = [firstLine]
    firstLine = firstLine.split(' ')
    T = int(firstLine[0])
    Q = int(firstLine[1])
    N = int(firstLine[2])
    for i in range(T+Q+N):
        line = raw_input()
        fileInput.append(line)
    topicInfo = []
    topicQues = {}
    
    #topic geo info
    for i in range(T):
        curLine = fileInput[1+i].split(' ')
        topicInfo.append([int(curLine[0]), float(curLine[1]), float(curLine[2])])
        topicQues[int(curLine[0])] = []
    
    #topicQuestion indexing
    for i in range(Q):
        curLine = fileInput[1+T+i].split(' ') 
        quesId = int(curLine[0])
        nOfTop = int(curLine[1])
        topicList = [int(k) for k in curLine[2:]]
        for j in topicList:
            (topicQues[j]).append(quesId)
        
    #queryProcessing
    for i in range(N):
        curLine = fileInput[1+T+Q+i].split(' ')
        curPos = (float(curLine[2]),float(curLine[3]))
        nearTopics = getNearTopics(curPos,topicInfo)
        queryType = curLine[0]
        queryNum = int(curLine[1])
        output = ""
        if queryType=='t':
            for j in nearTopics[:queryNum]:
                output = output + str(j) + " "
        elif queryType=='q':
            nearQues = getNearQuestions(nearTopics,topicQues)
            for j in nearQues[:queryNum]:
                output = output + str(j) + " "
                
        print output[:-1]