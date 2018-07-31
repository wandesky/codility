# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    miny = 1
    leny = len(A)

    if(leny < 1 or max(A) < 1):
        return 1

    sorty = sorted(A)
    # print('sorty is ', sorty)
    for i in range(0, leny, 1):
        if(sorty[i] > miny):
            return miny
        elif(sorty[i] == miny):
            miny += 1

    return miny
    
