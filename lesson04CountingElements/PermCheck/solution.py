# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    lengthy = len(A)
    sorty = sorted(A)
    # print('sorty is, ',sorty)
    if(lengthy == 0 or sorty[0] != 1):
        return 0
    elif(lengthy == 1 and sorty[0] != 1):
        return 1
    
    # maxy, miny = max(A), min(A)    
    for i in range(0, lengthy, 1):
        # print('sorty [i] and i+1', sorty[i], i+1)
        if (sorty[i] != i+1):
            return 0
            
    return 1