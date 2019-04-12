#Patrick Brannan - Last Edited 4/12/2019

# Implementation of hash tables with chaining using strings
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size, num_items):  
        self.item = []
        while num_items > size:
            size = (size*2)+1
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):  #helps determine b --- how/why?
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

#PROBLEM 2
def ReadFile1(F):   #There are about 400,000 different words in the file
  f = open('glove.6B.50d.txt',encoding='utf-8')
  for line in f:
      F.append(line)
  return F
  
  
#PROBLEM 4  
def ReadFile2(F2):
    o = open('wordpairing.txt', "r")
    for line in o:
        F2.append(line)
    return F2



#Problem 1
#print('Choose Table Implentation')  
#print('Type 1 for BST, or 2 for Hash Table with Chaining')
#selection = input()
#work = selection
#int(selection, 10)
#print('test', work)
#print(work)

#if work == 1:   #BST WORK
 #   print('WIP')
    
    
#PROBLEM 2
F = []
ReadFile1(F)
E = HashTableC(53, len(F))  #Load Factor is Number of entries/Number of buckets
for f in F:
    InsertC(E, f, len(f))
#END OF NUMBER 2
#Number 3
print('Hash table stats:')
print('Initial Table Size:', 53)
print('Final Table Size:', len(E.item))
load_factor = len(F)/len(E.item)
print('Load factor:', load_factor)
print('Percentage of empty lists:', (1-load_factor)*100, '%')
print('Standard deviation of the lengths of the lists:') #What is being asked for exactly?


#START OF NUMBER 4
F2 = []
ReadFile2(F2)
print(F2[0])
print(F2[1])
