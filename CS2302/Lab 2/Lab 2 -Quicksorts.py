#Patrick Brannan 2/22/2019
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

#Quick Sort - Use first element as a pivot
def Quicksort(L, end):
  if L == end:
    return L
  
  temp = L
  endtemp = end

  pivot = Partition(L, end, temp, endtemp)
  if endtemp != pivot:
    tmp = temp
    while tmp.next != pivot:
      tmp = tmp.next
    tmp.next = None

    temp = Quicksort(temp, tmp)

    tmp = temp.tail
    tmp.next = pivot
  pivot.next = Quicksort(pivot.next, endtemp)

  return endtemp


def Partition(L, end, temp, endtemp):
  pivot = end
  previous = None ###
  current = L
  test = pivot ###RENAME

  for j in range(start, end):
    #checks if element is smaller/equal to pivot
    if temp <= pivot:

      i=i+1
      L.head.item = L.tail.item
      L.tail.item = temp.item
      L[i], L[j] = L[j], L[i]
  L[i+1], L[end] = L[end], L[i+1]

  return(i+1)



#CALLS
L = List()
n = 5                           #n is total of numbers printed from 0
for i in range(n):
    x = random.randint(0, 100)     #Only two Digits
    Append(L, x)
Print(L)

print(L.head.item)



Quicksort(L.head, L.tail)
