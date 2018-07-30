'''
The solution is correct but fails the time complexity text. Currently it works at O(N**N) yet the problem wants an O(N)
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    #create permutation list of range (1,X+1)
    #for every i in A, check if permlist is a subset of A
    #  return i 
    #else return -1
    
    permlist = [i for i in range(1, X+1)]
    lenA, lenPerm = len(A), X
    tempA = A[:lenPerm-1]
    
    for i in range(lenPerm-1, lenA, 1):
        tempA.append(A[i])
        if(set(permlist).issubset(set(tempA))):
            return i
            
    return -1