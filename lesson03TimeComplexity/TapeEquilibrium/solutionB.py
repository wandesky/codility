'''
This solution worked out because it has a time complexity of O(N)
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    lengthy = len(A)
    if (lengthy == 0 or lengthy == 1):
        return 0
        
    diffies =[]
    maxy = sum(A)
    tempy = 0
    
    for i in range(0, lengthy-1, 1):
        tempy = tempy + A[i]
        diffies.append(abs(maxy-tempy-tempy))
        
        print('diffies ',diffies)
    # print(min(diffies))
    return(min(diffies))