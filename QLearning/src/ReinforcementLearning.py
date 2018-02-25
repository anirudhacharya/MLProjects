'''
Created on Oct 6, 2013

@author: Anirudh
'''
from QLearningAgent import QLearningAgent
import matplotlib.pyplot as pyplot

def main():
    r43 = -0.04
    qGrid43 = QLearningAgent([[r43, r43, r43, +1],
                              [r43, None, r43, -1],
                              [r43, r43, r43, r43]],
                            (0,0),
                            [(3, 2), (3, 1)],
                            0.9,#gamma
                            0.60, #alpha
                            10,  #N_e
                            0.6, #epsilon, greater the value of epsilon greater the random actions
                            2) #rewardPlus
    
    #Another Trial Grid
    r33 = -3
    qGrid33 = QLearningAgent([[r33, -1, 5],
                              [-1, -1, -1],
                              [-1, -1, -1]],
                            (0,0),
                            [(2,2)],
                            0.9,#gamma
                            0.10, #alpha
                            30,  #N_e
                            0.9, #epsilon, greater the value of epsilon greater the random actions
                            2) #rewardPlus
    
    qGridToRun = qGrid43
    
    iterations = 500
    x = []
    y1 = []
    y2 = []
    y3 = []
    for i in range(iterations):
        curState = qGridToRun.initialState
        while curState not in qGridToRun.terminals:
            a = qGridToRun.getActionToPerform(curState)
            #a = qGridToRun.getAlternateActionToPerform(curState)
            resultState = qGridToRun.doAction(curState, a)
            qGridToRun.N[(curState,a)] += 1
            qGridToRun.makeUpdate(resultState, curState, a) 
            curState = resultState
        qGridToRun.Q[(curState,a)] = qGridToRun.getRewards(curState)
        x.append(i)
        y1.append(qGridToRun.Q[(2,2),(1,0)])
        y2.append(qGridToRun.Q[(0,0),(0,1)])
        y3.append(qGridToRun.Q[(0,2),(1,0)])
    
    plotRMS(x,y1,'r')
    plotRMS(x,y2,'b')
    plotRMS(x,y3,'g')
    pyplot.show()
        
    for s in qGridToRun.allStates:
        if s not in qGridToRun.terminals:
            print s, qGridToRun.getActionToPerform(s)
    
def plotRMS(x,y,c):
    avg = sum(y)/len(y)
    rmsV = []
    for i in y:
        rmsV.append(((i-avg) ** 2) ** 0.5)
    pyplot.plot(x,rmsV,c)

if __name__ == '__main__':
    main()    