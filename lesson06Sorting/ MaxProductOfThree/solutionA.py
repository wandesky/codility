'''
This one definately has problems, just ran out of time and pushed it. The question also has a problem, 2,4,5 is not the maximum, 2,5,6 is the maximum
Report the above error to codility
On a second look, the question appears to be fine. The 2,4,5 appear to be referring to the indices of values 2,5,6.
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sorty = sorted(A)
    # print('sorty ', sorty)
    bigy3 = sorty[-3:]
    
    # print('bigy3 ', bigy3)

    multy = 1
    
    #Check if any of all bigy3 numbers are positive
    # maxy = max(bigy3)
    for i in range(0, 3, 1):
        if (bigy3[i] >= 1):
            nicey = True
            multy *= bigy3[i]
        else:
            nicey = False
            
    if (nicey):
        return multy
    else:
        return notnicey(sorty)
        
def notnicey(sorty):
    miny = sorty[0]
    smally = miny
    
    for i in range(0, len(sorty), 1):
        if (sorty[i] > smally and sorty[i] <= 0):
            smally = sorty[i]
    indy = sorty.index(smally)
    
    return (sorty[indy] * sorty[indy-1] * sorty[indy-2])
            