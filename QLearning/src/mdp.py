'''
Created on Oct 5, 2013

@author: Anirudh
'''
import abc

class MDP:
    __metaclass__ = abc.ABCMeta
    def __init__(self, rewards, initialState, actionList):
        self.initialState = initialState
        self.rewards = rewards # the stateSpace can be got by rewars.keys()
        self.actionList = actionList
        pass
    
    @abc.abstractmethod
    def getTransitionModel(self, state, action):
        """gives a transition model for a learned mdp model. Enter the state and 
        action. The output will be result state and the robability with which it 
        will reach the state"""
        return
    
    def getRewards(self, state):
        """Given a state it will putput the reward for that state"""
        return self.rewards[state]
    
    @abc.abstractmethod
    def getPossibleActions(self, state):
        """Outputs the allowed actions in a particular state."""
        return