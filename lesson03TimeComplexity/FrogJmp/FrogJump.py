# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(X, Y, D):
    # write your code in Python 3.6
    
    #catch the usual suspects/scenarios
    #substract x from y resulting to z
    #if z is greater than d,
    # then ceil(z/d) else return 1
    
    if (X==Y):
        return 0
        
    z = Y-X
    
    if (z > D):
        return math.ceil(z/D)
    else:
        return 1
    