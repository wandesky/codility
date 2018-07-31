# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if(len(A) == 0):
        return 0
    #the two lines below forget to catch A[0] == 0
    # if(len(A) == 1):
        # return A[0]
    setty = set(A)
    leny = len(setty)
    return leny