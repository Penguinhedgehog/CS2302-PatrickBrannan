#Patrick Brannan
#Last Edited on 5/11/2019 - Due 5/9/2019
#For this program, we are implementing a trigonometric functions with random values
#And we are finding the partitions of a list using backtracking.
import math
import mpmath
import random
import numpy as np

#Part 1, randomized algorithm
def random_trig(x):
    print('Random Value between -pi and pi is:', x)
    print('FINDING VALUES FOR:')
    print('sin(t):           ', math.sin(x))
    print('cos(t):           ', math.cos(x))
    print('tan(t):           ', math.tan(x))
    print('sec(t):           ', mpmath.sec(x))
    print('-sin(t):          ', -math.sin(x))
    print('-cos(t):          ', -math.cos(x))
    print('-tan(t):          ', -math.tan(x))
    print('sin(-t):          ', math.sin(-x))
    print('cos(-t):          ', math.cos(-x))
    print('tan(-t):          ', math.tan(-x))
    print('sin(t)/cos(t):    ', math.sin(x)/math.cos(x))
    print('2sin(t/2)cos(t/2):', 2*math.sin(x/2)*math.cos(x/2))
    print('sin^2(t):         ', math.pow(math.sin(x), 2))
    print('1-cos^2(t)        ', 1 - math.pow(math.cos(x), 2))
    print('(1-cos(2t))/2:    ', (1 - math.cos(2*x))/2)
    print('1/cos(t):         ', 1/math.cos(x))

#Part 2, backtracking subset sum
def backtracking(S, S1):    #Need recursion
    goal = sum(S)//2
    if sum(S)%2 == 1:
        print('The list sum is odd, and cannot be splot between two subsets.')
        return [], []
    else:
        for s in S:
            if s not in S1:
                S1.append(s)
                if sum(S1) == goal:
                    S2 = []
                    for i in S:
                        if i not in S1:
                            S2.append(i)
                    print('Subset 1 is:', S1, 'and Subset 2 is:', S2) #may run several times
                    return
                elif sum(S1) > goal:
                    S1.remove(S1[-1])
                    S1.remove(S1[-1])
                    return S1
                else:
                    backtracking(S, S1)
    print('The list cannot be divided into two equal subsets. - No partition exists')   #May also display twice
    return
            

#Part 1 - creates random value
t = np.random.uniform(-math.pi, math.pi)
random_trig(t)
print()

#Part 2 - creates and tests 3 different sets for subset sum
S1 = {2, 4, 5, 9, 12}
backtracking(S1, [])
print()

S2 = {2, 4, 5, 9, 13}
backtracking(S2, [])
print()

S3 = {2, 4, 5, 9, 14}
backtracking(S3, [])