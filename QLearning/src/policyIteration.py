'''
Created on Sep 30, 2013

@author: Anirudh
'''
from gridMDP import gridMDP

def policyIteration(mdp):
    U = {}
    policy = {}
    for s in mdp.allStates:
        if s in mdp.terminals:
            U[s] = mdp.rewards[s]
            policy[s] = (0,0)
        else:
            U[s] = 0
            policy[s] = (0,1)  #default policy is to go up in the grid
    while True:
        U = policyEvaluation(policy, U, mdp)
        unchanged = True
        for s in mdp.allStates:
            if s not in mdp.terminals:
                bestExpected = 0
                preferredAction = (0,0)
                for a in mdp.actionList:
                    expectedUtility = 0
                    for (s1,p) in mdp.getTransitionModel(s,a):
                        expectedUtility = expectedUtility + (p*U[s1])
                        if expectedUtility > bestExpected:
                            bestExpected = expectedUtility
                            preferredAction = a
                if preferredAction != policy[s]:
                    policy[s] = preferredAction    #We improve the policy for state s to action a
                    unchanged = False
        if unchanged:
            return U, policy
    return

def policyEvaluation(policy, U, mdp):
    rewards, gamma = mdp.rewards, mdp.gamma
    for s in mdp.allStates:
        if s not in mdp.terminals:
            U[s] = rewards[s]+(gamma * sum([p * U[s1]
                                              for (s1, p)
                                              in mdp.getTransitionModel(s, policy[s])]))
    return U

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
    gridToRun = grid33
    finalUtilities, optimalPolicy = policyIteration(gridToRun)
    gridToRun.printUtilities(finalUtilities)
    gridToRun.printPolicy(optimalPolicy)

if __name__ == '__main__':
    main()