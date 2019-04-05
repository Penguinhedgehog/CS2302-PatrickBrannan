#Patrick Brannan - Last Edited 4/5
#Only Question 1 is Unfinished.
import numpy as np
import matplotlib.pyplot as plt
import math

#BST CODE
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

#Question 2
def Search(T, k):
  if T is None:
    print('Not found')
    return
  elif k == T.item:
    print('Found', k)
    return
  elif k < T.item:
    return Search(T.left, k)
  else:
    return Search(T.right, k)


#QUESTION 3 WIth a SORTED LIST, create a Binary tree
def BuildTree(A):
  if len(A) == 1:
    B = BST(A[0])
    return B
  else:
    B = BST(A[0])
    B.right = BuildTree(A[1:])
    return B


#Question 4 - Extract elements into a sorted list
def SortedList(T, newarray):
  if T is not None:
    SortedList(T.left, newarray)
    newarray.append(T.item)
    SortedList(T.right, newarray)

#Question 5 - Print the nodes and sort by depth
def PrintDepth(T, depth):
  if T is None:
    return
  elif depth == 0:
    print(T.item, end = " ")
  else:
    PrintDepth(T.left, depth - 1)
    PrintDepth(T.right, depth - 1)

#GRAPHING CODE ---- ALSO NUMBER 1 - UNFINISHED
def circle(center, rad):
  n = int(4*rad*math.pi)    
  t = np.linspace(0,6.3,n) 
  x = center[0] + rad*np.sin(t)  
  y = center[1] + rad*np.cos(t)   
  return x, y

def draw_circle(ax, center, radius):
    x,y = circle(center,radius)
    ax.plot(x, y, color='k')
    ax.fill(x, y, "k") 

def insert_text(x,y, text):
  plt.text(x-20 , y-10, text, color='w')

#MAKE TREE SHAPES
def tree(ax,n,a, b, c, x, T):
  if n>0:

    if T is not None:


      p = np.array([a, b, c])
      ax.plot(p[:,0],p[:,1],color='k')

      #Make on left
      x = x*.5
      bl = a
      cl = [a[0] + x, a[1]-250]
      al = [a[0] - x, a[1]-250]
      tree(ax, n-1, al, bl, cl, x, T.left)

      draw_circle(ax, b, 30)
      insert_text(b[0], b[1], T.item)
      
      #Make on right
      br = c
      ar = [c[0] + x, c[1]-250]
      cr = [c[0] - x, c[1]-250]
      tree(ax, n-1, ar, br, cr, x, T.right)

  
#SETUP
plt.close("all")
# Code to test the functions above
T = None
A = [10, 4, 15, 2, 8, 12, 18, 1, 3, 5, 9, 7]
for a in A:
    T = Insert(T,a)

#NUMBER 1 - UNFINISHED
a, b, c = [700, 750], [1000, 1000], [1300, 750]
x = 300
fig, ax = plt.subplots()
n = 5  #layers of trees

tree(ax, n, a, b, c, x, T)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('BST.png')

#NUMBER 2
print('QUESTION 2 ----------')
Search(T, 8)

#Number 3   - List MUST be sorted
print('QUESTION 3 ----------')
three = [1, 3, 5, 6, 8, 10, 14, 16]
#BuildTree(three)
InOrderD(BuildTree(three), '')

#Number 4
print('QUESTION 4 ----------')
four = []
SortedList(T, four)
for i in range(len(four)):
  print(four[i], end = " ")
print()

#Number 5
print('QUESTION 5 ----------')
depth = 4          #Based on the lowest Depth in the current tree
for i in range(depth+1):
  print('Keys at depth', i, ':', end = " ")
  PrintDepth(T, i)
  print()
