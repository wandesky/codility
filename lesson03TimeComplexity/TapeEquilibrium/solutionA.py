'''
Failed complexity test, the code below returt O(N*N) yet the question wants O(N)
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    lengthy = len(A)
    if (lengthy == 0 or lengthy == 1):
        return 0
        
    diffies =[]
    
    for i in range(1, lengthy, 1):
        lefty, righty = A[:i], A[-(lengthy-i):]
        # print('lefty', lefty)
        # print('righty', righty)
        sumlefty, sumrighty = sum(lefty), sum(righty)
        # print('sumlefty', sumlefty)
        # print('sumrighty', sumrighty)
        absdiffy = abs(sumlefty-sumrighty)
        diffies.append(absdiffy)
        # print('diffies ',diffies)
    # print(min(diffies))
    return(min(diffies))