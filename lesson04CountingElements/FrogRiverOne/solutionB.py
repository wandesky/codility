'''
This solution has complexity O(N)
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    permset = set()
    
    for i in range(0, len(A), 1):
        if(A[i] <= X and A[i] >= 1):
            permset.add(A[i])
            if (len(permset) == X):
                return i
            
    return -1