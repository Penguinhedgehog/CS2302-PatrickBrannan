#Patrick Brannan 3/3/2019
import random
#First class - NODE
class Node(object):        #CONSTRUCTER
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 

#PRINT STATEMENTS
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)

#2nd class - LIST
class List(object):
  def __init__(self): 
        self.head = None
        self.tail = None

def IsEmpty(L):
  return L.head == None   #CHECKS IF EMPTY - default True?

def Append(L, x):       #Inserts X at the end
    if IsEmpty(L):        #Places Node if list is empty
       L.head = Node(x)
       L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  #Makes a new Line

def Median(L):
  C = Copy(L)
  Sort(C)
  return ElementAt(C,GetLength(C)//2)

#MERGE SORT
def Mergesort(L, n):
  temp = L
  if L is None:
    print('reaches Endpoint 1')
    #return L
  elif L.next is None:
    print('ENdpoint 2')
    return L
  else:
    middle = getMiddle(L)
    middleN = middle.next
    middle.next = None


    left = Mergesort(temp, n//2)   #mergesort left and right sides
    print(left.item, 'left')
    right = Mergesort(middleN, n//2)
    print(right.item, 'right')
    sort = PutTogether(left, right)
    print(sort.item, '1st OF SORTED LIST')
    return sort
  
def PutTogether(left, right):
    if left is None:
      return right
    elif right is None:     #Returns left or right
      return left
    elif left.item <= right.item:
      order = left
      order.next = PutTogether(left.next, right)
    else:
      order = right
      order.next = PutTogether(left, right.next)
    print(order.item, 'Order Item?')
    return order

def getMiddle(M):
  fast = M.next
  slow = M
  while fast is not None:
    fast = fast.next
    if fast is not None:
      slow = slow.next
      fast = fast.next
  return slow

#CALLS
L = List()
n = 5                           #n is total of numbers printed from 0
for i in range(n):
    x = random.randint(0, 100)     #Only two Digits
    Append(L, x)
Print(L)

print(L.head.item)


#MERGE SORT
Mergesort(L.head, n-1)
Print(L)

#MERGE SORT END


