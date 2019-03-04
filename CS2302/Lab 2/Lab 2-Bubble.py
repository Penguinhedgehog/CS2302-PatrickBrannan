#Patrick Brannan 2/3/2019
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

def Median(L, n):
  if n > 0:
    return Median(L.next, n-1)
  else:
    return L.item



#SORTS
def Bubblesort(L, n):
  temp = L
  if n>0:
      if temp.item > temp.next.item:
        temp2 = L.item             #Breaks when using regular temp
        L.item = L.next.item
        L.next.item = temp2
        #temp = temp.next
        Bubblesort(temp.next, n-1)
      else:
        #temp = temp.next
        Bubblesort(temp.next, n-1)
  for i in range(n):          #Runs Bubble sort until its fully sorted
    Bubblesort(L, n-1)

#CALLS
L = List()
n = 5                           #n is total of numbers printed from 0
for i in range(n):
    x = random.randint(0, 100)     #Only two Digits
    Append(L, x)
Print(L)



#BUBBLE SORT
Bubblesort(L.head, n-1)
Print(L)
print('Median:', Median(L.head, n//2))
#END OF BUBBLE SORT


