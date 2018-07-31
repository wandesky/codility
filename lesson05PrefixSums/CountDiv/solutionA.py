# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    if K == 0:
        print('terrible mistake, someone is trying to divide by 0')
        return 0

    result = 0
    biggyfound = smallyfound = False
    upperbonus = lowerbonus = 0
    if(A % K == 0):
        lowerbonus += 1
        smally = A
        smallyfound = True
        # print('lowerbonus awarded')
    if(B % K == 0):
        upperbonus += 1
        biggy = B
        biggyfound = True
        # print('upperbonus awarded')
        
    if(lowerbonus < 1):
        for a in range(A, (A+K+1), 1):
            if(a % K == 0):
                smally = a
                # print('smally is', smally)
                smallyfound = True
                # print('smally found')
                break
    if(upperbonus < 1):
        for b in range(B, (B-(K+1)), -1):
            # print('b is ', b)
            if(b % K == 0):
                biggy = b
                # print('biggy is', biggy)
                biggyfound = True
                # print('biggy found')
                break
    if(upperbonus == 1 and lowerbonus == 1):
        result = 1 + ((biggy - smally) / K)
    elif(biggyfound and smallyfound and (upperbonus != 1 and lowerbonus != 1)):
        result = 1 + lowerbonus + upperbonus + ((biggy - smally) / K)
    elif(biggyfound and smallyfound):
        result = lowerbonus + upperbonus + ((biggy - smally) / K)
    else:
        print('the last else was executed')
        result = lowerbonus + upperbonus
    
    return int(result)