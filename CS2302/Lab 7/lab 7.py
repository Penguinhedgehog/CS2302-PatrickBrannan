#Patrick Brannan
#Last Edited 5/4/2019
#Purpose of program is work on traversing the graph using BFS and DFS, while 
#   also creating a Adj. List.

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def draw_maze(walls,maze_rows,maze_cols,path, cell_nums=False):
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
    
    if cell_nums:  #Changed to only draw the numbers along the path
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols  
                if cell in path:
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

#Problem 1
def user_input_maze(S, walls, r, c, m):             #walls is the list of walls of maze
    n = r*c
    remove = m
    while NumSets(S) != 1 and remove > 0:
        wall = random.randint(0,len(walls)-1)   #holds the wall value for later
        w = walls[wall]
        temp = union(S, w[0], w[1])
        if temp == True:
            walls.pop(wall)
            remove -= 1
    while remove > 0:
        wall = random.randint(0,len(walls)-1)
        walls.pop(wall)
        remove -= 1
    draw_maze(walls, r, c, [])
    if m < n-1:
        print('A path from the source to the destination is not guaranteed to exist')
    elif m == n-1:
        print('There is a unique path from source to destination')
    else:
        print('There is at least one path from source to destination')

#Problem 2
def adj_list(walls_left, base, n):    #Search for missing walls, if walls are missing, add the two cells to list
    adj = []
    for i in range(n):
        adj.append([])
        
    for i in walls_left:
        base.remove(i)
    
    for i in range(len(base)):
        adj[base[i][0]].append(base[i][1])
        adj[base[i][1]].append(base[i][0])
    return adj
    
##Problem 3
##BREADTH FIRST SEARCH  -- #DO NOT USE RECURSION
def bfs(G, start, end):
    queue = []
    output = [0]
    current = start
    
    while output[-1] != end:
        for g in G[current]:
            if g not in output:
                queue.append(g)
                output.append(g)
        current = queue[0]
        queue.remove(current)
    return output
    
    
##Depth first search  - NO  RECURSION
def dfs(G, start, end):
    stack = [start]
    output = [start]
    while output[-1] != end:
        i = 0
        while G[stack[-1]][i] in output:
            i += 1
            if i == len(G[stack[-1]]):
                stack.pop()
                i = 0
        output.append(G[stack[-1]][i])
        stack.append(G[stack[-1]][i])         
    return output
   
#DFS - WITH RECURSION         
def dfs_recursive(G, stack, output, end):
    if output[-1] != end:
        i = 0
        while G[stack[-1]][i] in output:
            i += 1
            if i == len(G[stack[-1]]):
                stack.pop()
                i = 0
        output.append(G[stack[-1]][i])
        stack.append(G[stack[-1]][i])
        dfs_recursive(G, stack, output, end)
        
    return output




plt.close("all") 
rows = 5
col = 10
n = rows*col
print('CREATING MAZES WITH DIMENSIONS', rows, 'X', col)

#Start of randomized maze
M = DisjointSetForest(rows*col)
walls = wall_list(rows,col,M)
baseblock = wall_list(rows, col, M)

#Problem 1
m = int(input('Choose a number of walls to remove: '))
user_input_maze(M, walls, rows, col, m)

#Problem 2
G = adj_list(walls, baseblock, n)
print('Adjacency list is:', G)

#Here after the base maze is displayed, three more mazes will appear and display what was traversed
#PROBLEM 3
end = n-1
#BFS WORKS
start = time.time()
bfslist = bfs(G, 0, end)
print('Items traversed using BFS:', bfslist)
print()
draw_maze(walls,rows,col, bfslist, cell_nums=True)
bfstime = time.time() - start

#DFS - normal
start = time.time()
dfslist = dfs(G, 0, end)
print('Items traversed using DFS:', dfslist)
print()
draw_maze(walls,rows,col, dfslist, cell_nums=True)
dfstime = time.time() - start

#DFS - recursive
start = time.time()
dfsr_list = dfs_recursive(G, [0], [0], end)
print('Items traversed by using DFS recursively:', dfsr_list)
draw_maze(walls,rows,col, dfsr_list, cell_nums=True)
dfsrtime = time.time() - start

print('BFS time with', n, 'size is:',bfstime)
print('DFS time with', n, 'size is', dfstime)
print('DFS with recurstion time with', n, 'size is', dfsrtime)