'''
This solution is correct. Gives O(N+M)
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    if(not len(A)):
        return [0]*N
    
    counter = [0]*N
    maxy = 0
    miny = 0
    # print('N is ', N)
    for elem in A:
        if(elem >= 1 and elem <=N and counter[elem-1] < miny):
            counter[elem-1] = miny
        if(elem >= 1 and elem <=N):
            counter[elem-1] += 1
            if(counter[elem-1] > maxy):
                maxy = counter[elem-1]
            # print(' counter is ', counter)
            
        elif(elem == N + 1):
            miny = maxy
            # print(' miny is ', miny)
            
    for i in range(0, N, 1):
        if(counter[i] < miny):
            counter[i] = miny
        # print('when i is {0}, counter becomes {1}'.format(i, counter))    
    return counter
    