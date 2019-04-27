#Patrick Brannan
#Last Edited 4/23/2019
#Purpose of program is to create a random maze of given dimensions
import matplotlib.pyplot as plt
import numpy as np
import random
import time

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    
    if cell_nums:
        for r in range(maze_rows):
            #print('ROW:', r)
            for c in range(maze_cols):
                #print('COLUMN:', c)
                cell = c + r*maze_cols   
                #print('CELLS:', cell)
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols, S):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1      
  
def find(S,i):
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i):
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j): #joins set if different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    else:
        return False
         
def union_by_size(S,i,j):
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: 
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
        return True
    else:
        return False
            

def NumSets(S):
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count

#THE TWO METHODS FOR CREATING THE MAZES

def single_maze(S, walls, r, c): 
    while NumSets(S) != 1:
        wall = random.randint(0,len(walls)-1)   #holds the wall value for later
        w = walls[wall]
        temp = union(S, w[0], w[1])
        if temp == True:
            walls.pop(wall)
    draw_maze(walls,r,c)

#Exact same as previous method except it uses Union by size
def single_maze_c(S, walls, r, c):
    while NumSets(S) != 1:
        wall = random.randint(0,len(walls)-1)   
        w = walls[wall]
        temp = union_by_size(S, w[0], w[1])
        if temp == True:
            walls.pop(wall)
    draw_maze(walls,r,c)


plt.close("all") 
rows = 10
col = 15
print('CREATING MAZES WITH DIMENSIONS', rows, 'X', col)
#Important to Note that I edited the union methods to return T/F
#Start of randomized maze
M = DisjointSetForest(rows*col)
walls = wall_list(rows,col,M)
draw_maze(walls,rows,col,cell_nums=True) #Prints the base block for maze

start = time.time()
single_maze(M, walls, rows, col)
end = time.time()
run_time_1 = end - start


#Start on maze with size/compression - differentiates it from first maze
M_c = DisjointSetForest(rows*col)
walls_c = wall_list(rows,col,M_c)

start = time.time()
single_maze_c(M_c, walls_c, rows, col)
end = time.time()
run_time_2 = end - start

print('Running time for creating a random maze:', run_time_1)
print('Running time for maze with union by size and compression:', run_time_2)