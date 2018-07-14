'''
Created on Jun 12, 2014

@author: Anirudh
'''
import numpy as np

class Sudoku:
    def __init__(self, grid):
        '''
        Initializes the sudoku grid, grid is a list of 9x9
        '''
        self.grid = np.asarray(grid)
        
        return
    
        