# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#my test case that should return 14
# [0,1,1,1,1,0,0,0,0,1,1]

def solution(A):
    # write your code in Python 3.6
    
    i = 0
    lengthy = len(A)
    summy = 0
    tempy = 0
    tempcount = 0
    multy = 1
    
    while(i < lengthy - 1):
        #looking for first eastbound car without adjacent westbound car
        if(A[i] == 0 and A[i+1] != 1):
            multy += 1
            i += 1
        #looking for first eastbound car with adjacent westbound car
        elif(A[i] == 0 and A[i+1] == 1 and i+1 <= (lengthy - 1)):
            tempcount = 0
            #set index at first detected westbound car
            tempy = i+1
            #start counting adjacent westbound cars
            while(tempy <= lengthy - 1 and A[tempy] == 1):
                tempcount += 1
                tempy += 1
            #first multiply the tempcount with all possible 0s that could see the counted 1s
            #then update summy (the sum of all possible pairs(P,Q)
            summy += tempcount * multy
            #return -1 if number of pairs exceeds 1,000,000,000
            if(summy > 1000000000):
                return -1
            multy += 1
            i = tempy
        else:
            i += 1
    return summy