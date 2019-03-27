#Patrick Brannan
#Last Modified 3/26/2019
class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
#WORK GOES HERE -------------------------------
#Question 1
def TreeHeight(T):
  if T.isLeaf:
    return 1
  else:
    return 1 + TreeHeight(T.child[0])

#Question 2
def SortedList(T, newList):   
  if T.isLeaf:
    for i in range(len(T.item)):
      newList.append(T.item[i])
  else:
    for i in range(len(T.child)):    #Gets the child of each node
      if i > 0:                  #Prints the node as you traverse
        newList.append(T.item[i - 1])
      SortedList(T.child[i], newList)
    return newList

#Question 3
def MinimumElementD(T, d):
  if d == 0:
    return T.item[0]
  elif T.isLeaf:
    return -1
  else: 
   return MinimumElementD(T.child[0], d-1)

#Question 4
def MaxAtD(T, d):
  if d == 0:
    return T.item[-1]
  elif T.isLeaf:
    return -1
  else: 
   return MaxAtD(T.child[-1], d-1)

#Question 5
def NodesAtDepth(T, d):
  nsum = 0
  if d == 0:
    return 1
  elif T.isLeaf:
    return 0
  else:
    for i in range(len(T.child)):
      nsum += NodesAtDepth(T.child[i], d-1)
    return nsum

#Question 6
def PrintAtDepth(T, d):   
  if d == 0:
    for i in range(len(T.item)):
      print(T.item[i])
  elif T.isLeaf:
    return
  else:
    for i in range(len(T.child)):
      PrintAtDepth(T.child[i], d-1)
    return

#Question 7
def FullNodes(T): 
  if T.isLeaf:
    if T.max_items == len(T.item):
      return 1
    else:
      return 0
  else:
    fNodes = 0
    if T.max_items == len(T.item):
      fNodes += 1
      for i in range(len(T.item)):
        fNodes += FullNodes(T.child[i])
    else:
      for i in range(len(T.item)):
        fNodes += FullNodes(T.child[i])
    return fNodes

#Question 8
def FullLeaves(T): 
  if T.isLeaf:
    if T.max_items == len(T.item):
      return 1
    else:
      return 0
  else:
    fLeaves = 0
    for i in range(len(T.item)):
      fLeaves += FullLeaves(T.child[i])
    return fLeaves

#Question 9
def FindDepth(T, k):
  if T.isLeaf:
    for i in range(len(T.item)):
      if T.item[i] == k:
        return 0
    return -1           ##Must be more consistant with varying tree size.
  else:
    depth = len(T.item)
    for i in range(len(T.item)):
      if T.item[i] == k:
        return 0
    for i in range(len(T.child)):
      depth = 1 + FindDepth(T.child[i], k)
    return depth


L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5, 105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
  Insert(T, i)
PrintD(T, ' ')    #Shows tree

#Question 1 - Find the height
print('The Tree height is:', TreeHeight(T))

#Question 2 - Make a sorted list
newList = []
print('The sorted list is: ', SortedList(T, newList))

#Question 3 - Return the minimum element at a Depth
#Head node starts at depth 0 
depth = 2

print('The minimum of D',depth, 'is:', MinimumElementD(T, depth))

#Question 4 - Return the max at a depth
print('The maximum of D',depth, 'is:', MaxAtD(T, depth))

#Question 5 - Return the # of nodes at depth
print('Nodes at the depth',depth,'----', NodesAtDepth(T, depth))

#Question 6 - Prints all the items at depth
print('#################################')
print('The following items are found in depth', depth)
PrintAtDepth(T, depth)
print('#################################')

#Question 7 - Returns # of full Nodes in tree (MAX size is 5)
print('The number of full nodes are:', FullNodes(T))

#Question 8 - Returns # of full Leaves in tree
print('The number of full leaves are:', FullLeaves(T))

#Question 9 - Return the depth at which you find the key
key = 60
print('Key', key, 'is at depth:', FindDepth(T, key))
        #PROBLEM - WILL NOT RETURN -1 IF KEY IS NOT FOUND.