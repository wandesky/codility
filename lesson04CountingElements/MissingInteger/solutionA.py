'''
This solution sucks. It doesnt work (especially when A is [-1000000, 1000000])
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    setty = set(A)
    listy = list(setty)
    sorty = sorted(listy)
    # print('sorty is ', sorty)
    
    miny, maxy = min(sorty), max(sorty)
    if(maxy <= 0 or len(A) == 0):
        return 1
    elif(miny > 1):
        return 1
        
    perm = [i for i in range(miny, maxy+1, 1)]
    # print('perm is ', perm)
    lengthyP = len(perm)
    lengthyS = len(sorty)
    if(lengthyP == lengthyS):
        return maxy+1
    for i in range(lengthyS):
        # print('i is ', i)
        if(perm[i] != sorty[i]):
            # print (perm[i])
            return perm[i]
            
    return 1