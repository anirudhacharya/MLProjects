'''
Created on Sep 30, 2013

@author: Anirudh
'''
from gridMDP import gridMDP

def valueIteration(mdp, epsilon):
    U1 = {}
    policy = {}
    rewards, gamma = mdp.rewards, mdp.gamma
    for s in mdp.allStates:
        if s in mdp.terminals:
            U1[s] = mdp.getRewards(s)
            policy[s] = (0,0)
        else:
            U1[s] = 0
            policy[s] = (0,0)
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.allStates:
            if s not in mdp.terminals:
                preferredAction = (0,0)
                bestUtility = 0
                for a in mdp.actionList:
                    utility = 0
                    for (s1,p) in mdp.getTransitionModel(s,a):
                        utility = utility + (p*U[s1])
                        if utility > bestUtility:
                            bestUtility = utility
                            preferredAction = a
                U1[s] = rewards[s] + gamma * bestUtility
                policy[s] = preferredAction
                delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
            return U, policy

def main():
    r43 = -0.04
    grid43 = gridMDP([[r43, r43, r43, +1],
                      [r43, None, r43, -1],
                      [r43, r43, r43, r43]],
                     (0,0),
                     [(3, 2), (3, 1)],
                     0.99)
    r33 = -3
    grid33 = gridMDP([[r33, -1, 10],
                      [-1, -1, -1],
                      [-1, -1, -1]],
                     (0,0),
                     [(2,2)],
                     0.99)
    gridToRun = grid43
    finalUtilities, optimalPolicy = valueIteration(gridToRun, 0.1)
    gridToRun.printUtilities(finalUtilities)
    gridToRun.printPolicy(optimalPolicy)

if __name__ == '__main__':
    main()