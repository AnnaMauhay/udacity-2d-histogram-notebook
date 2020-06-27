#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    Sum = 0
    
    for row in range(0, len(grid)):
        blf=[]
        for col in range(0, len(grid[0])):
            if grid[row][col]==color:
                p=beliefs[row][col] * p_hit
            else:
                p=beliefs[row][col] * p_miss
            Sum = Sum + p
            blf.append(p)
            
        new_beliefs.append(blf)
        
    for row in range(0, len(new_beliefs)): 
        for col in range(0, len(new_beliefs[0])): 
            new_beliefs[row][col] = new_beliefs[row][col]/Sum
        
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    #pdb.set_trace()
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)