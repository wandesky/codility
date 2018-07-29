# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    #catch usual suspects/conditions
    #find maxy and miny values in A  (oldy)
    #create a newy list starting from miny to maxy having step 1
    #substracty newy from oldy to get singly
    #return singly[0]
    
    if (len(A) == 0):
        return 1
    elif (len(A) == 1):
        # if(A[0]==0):
        #     return 1
        if(A[0] == 1 or A[0] == 0):
            return A[0]+1
        else:
            return A[0]-1
        
    # print(max(A), min(A))
    maxy, miny = max(A), min(A)
    
    newy = [i for i in range(miny, maxy+1, 1)]
    # print('HEllo')
    # print('newy', newy)
    
    singly = list(set(newy).difference(set(A)))
    # print ('singly',singly[0])
    if(len(singly) < 1):
        if(miny > 1):
            return miny-1
        else:
            return maxy+1
    else:
        return singly[0]
    