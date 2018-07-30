'''
This one finally worked. 
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    counter = 1
    maxy, miny = max(A), min(A)
    sorty = sorted(A)
    if(maxy < 1 or len(A) == 0):
        return 1
    if(miny > 1):
        return 1
    for i in range(0, len(A), 1):
        if(counter == sorty[i]):
            counter += 1
        if(sorty[i] > counter):
            break
    return counter