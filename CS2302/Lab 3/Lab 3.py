#Patrick Brannan - Last Edited March 11
#Incomplete - Everything still needs to be done
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
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

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

#QUESTION 3 Have the array read through the beginning each time - Not Done
def BuildTree(A, B):
    if B is None:
      print('adding', A[0])
      B =  BST(A[0])

      for i in range(len(A) - 1):
        if A[i] < B.item:
         BuildTree(A[1:],B.left)  #Progresses through Array
        else:
          BuildTree(A[1:], B.right)

    elif A[0] < B.item:
      B.left = BuildTree(A, B.left)
      return
    else:
      B.right = BuildTree(A, B.right)
      return
    return B

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
InOrderD(T,'')
print()

#NUMBER 1
a, b, c = [700, 750], [1000, 1000], [1300, 750]
x = 300
fig, ax = plt.subplots()
n = 5  #layers of trees

tree(ax, n, a, b, c, x, T)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('WIP.png')


#NUMBER 2
Search(T, 8)

#Number 3 -WIP
test = [10, 4, 15]
B = None
InOrderD(BuildTree(test, B), '')
print()