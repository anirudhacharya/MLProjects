'''
Created on Sep 28, 2013

@author: Anirudh
'''
from MDP import MDP
import operator

class gridMDP(MDP):
    def __init__(self, grid, initialState, terminals, gamma):
        grid.reverse()
        self.grid = grid
        self.initialState = initialState
        self.gamma = gamma
        self.terminals = terminals
        self.noOfRows= len(grid)
        self.noOfCols = len(grid[0])
        self.allStates = []
        self.rewards = {}
        for x in range(self.noOfCols):
            for y in range(self.noOfRows):
                if grid[y][x] is not None:
                    self.allStates.append((x, y))
                self.rewards[(x,y)] = grid[y][x]
        self.actionList = [(1,0),(0,1),(-1,0),(0,-1)]
        MDP.__init__(self, self.rewards, initialState, self.actionList)
        #MDP, self).__init__(self.rewards, initialState, self.actionList)
    
    def getTransitionModel(self, state, action):
        if state in self.terminals:
            return [(state, 1.0)]
        if action is None:
            return [(state, 0.0)]
        else:
            return [(self.doAction(state, action), 0.8),
                    (self.doAction(state, self.rightOf(action)), 0.1),
                    (self.doAction(state, self.leftOf(action)), 0.1)]

    def rightOf(self, action):
        if action == (0,1):
            return (1,0)
        elif action==(1,0):
            return (0,-1)
        elif action==(0,-1):
            return (-1,0)
        elif action==(-1,0):
            return (0,1)
        else:
            return action
    
    def leftOf(self, action):
        if action == (0,1):
            return (-1,0)
        elif action==(1,0):
            return (0,1)
        elif action==(0,-1):
            return (1,0)
        elif action==(-1,0):
            return (0,-1)
        else:
            return action
    
    def getPossibleActions(self, state):
        return self.actionList
    
    def doAction(self, state, action):
            "Return the state that results from going in this direction."
            resultState = tuple(map(operator.add, state, action))
            if resultState in self.allStates:
                return resultState
            else:
                return state 
    
    def printUtilities(self, utilities):
        utilityMat = [['a' for t in range(self.noOfCols)] for q in range(self.noOfRows)]
        for i in range(self.noOfCols):
            for j in range(self.noOfRows):
                if (i,j) in utilities:
                    utilityMat[j][i] = utilities[(i,j)]
                else:
                    utilityMat[j][i] = 'None'
            utilityMat.reverse()
        for i in range(len(utilityMat)):
            print utilityMat[i]
            print '\n'
    
    def printPolicy(self, policy):
        for p in policy:
            if policy[p] == (0,1):
                policy[p] = '^'
            elif policy[p] == (1,0):
                policy[p] = '>'
            elif policy[p] == (0,-1):
                policy[p] = 'v'
            elif policy[p] == (-1,0):
                policy[p] = '<'
            else:
                policy[p] = '.'
            policyMat = [['a' for t in range(self.noOfCols)] for q in range(self.noOfRows)]
            for i in range(self.noOfCols):
                for j in range(self.noOfRows):
                    if (i,j) in policy:
                        policyMat[j][i] = policy[(i,j)]
                    else:
                        policyMat[j][i] = '.'
            policyMat.reverse()
        for i in range(len(policyMat)):
            print policyMat[i]
            print '\n'