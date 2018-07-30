'''
This solution is syntatically correct but fails the complexity test.  Gives O(N*M)
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    if(not len(A)):
        return [0]*N
    
    counter = [0]*N
    lengthy = len(A)
    # print('N is ', N)
    for elem in A:
        # print('elem is ', elem)
        if(elem >= 1 and elem <=N):
            counter[elem-1] += 1
            # print(' counter is ', counter)
        elif(elem == N + 1):
            counter = [max(counter)]*N
            # print(' counter is ', counter)
            
    return counter
    