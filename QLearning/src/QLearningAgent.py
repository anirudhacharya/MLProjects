'''
Created on Oct 4, 2013

@author: Anirudh
'''
from gridMDP import gridMDP
import random
import operator

class QLearningAgent(gridMDP):
    def __init__(self, grid, initialState, terminals, gamma, alpha, N_e, epsilon, rewardPlus):
        gridMDP.__init__(self, grid, initialState, terminals, gamma)
        self.alpha = alpha
        self.N_e = N_e
        self.Q = {}
        self.N = {}
        self.epsilon = epsilon
        self.rewardPlus = rewardPlus
        for i in self.allStates:
            for j in self.getPossibleActions(i):
                self.Q[(i,j)] = 0
                self.N[(i,j)] = 0
    
    #Overriding the transition Modle method, and returning junk values, becasue transition 
    #model should not be available to the learning agent.
    def getTransitionModel(self, state, action):
        return (state, 0)
    
    #Overriding the doAction method
    def doAction(self, state, action):
        stochasticProb = 0.8
        rightAction = self.rightOf(action)
        leftAction = self.leftOf(action)
        randomNumber = random.random()
        resultState = state
        if randomNumber <= stochasticProb:
            resultState = tuple(map(operator.add, state, action))
        elif randomNumber > stochasticProb and randomNumber < (stochasticProb + 
                                                               ((1-stochasticProb)/2)):
            resultState = tuple(map(operator.add, state, rightAction))
        else:
            resultState = tuple(map(operator.add, state, leftAction))
        
        if resultState not in self.allStates:
            resultState = state
        return resultState
    
    def getActionToPerform(self, curState):
        dictActions = {}
        for a in self.getPossibleActions(curState):
            if self.N[(curState,a)] < self.N_e:
                dictActions[self.rewardPlus] = a
            else:
                dictActions[self.Q[(curState,a)]] = a
        return dictActions[max(dictActions)]
    
    def getAlternateActionToPerform(self, state):
        dictActions = {}
        for a in self.getPossibleActions(state):
            dictActions[self.Q[(state,a)]] = a
        
        randomNumber = random.random()
        if randomNumber < self.epsilon:
            action = random.choice(self.getPossibleActions(state))
            if self.N[(state,action)] > self.N_e:
                return dictActions[max(dictActions)]
            else:
                return action
        else:
            return dictActions[max(dictActions)]
    
    #* self.N[(curState,action)] 
    def getUpdateValue(self, resultState, curState, action):
        value = self.alpha * (self.getRewards(curState) +
                              (self.gamma * self.getMaxQValue(resultState)) -
                              self.Q[(curState, action)])
        return value
    
    def makeUpdate(self, resultState, curState, actionTaken):
        updateValue = self.getUpdateValue(resultState, curState, actionTaken)
        self.Q[(curState,actionTaken)] += updateValue
        return
    
    def getMaxQValue(self, state):
        listOfQValues = []
        for i in self.getPossibleActions(state):
            listOfQValues.append(self.Q[(state, i)])
        return max(listOfQValues)