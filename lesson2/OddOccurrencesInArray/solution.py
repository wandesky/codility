# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    '''
    write your code in Python 3.6
    '''
    #catch the known scenarios
    # sort the array
    # check for similarity in adjacent bipolar elements
    # if two adjacent elements are not equal, return the smallest one
    # catch index out of bound error and return last item
    
    if(len(A) == 1):
        return A[0]
    elif(len(A) == 0):
        return 0
    
    # print('a is ', A)
    sortedA = sorted(A)
    # print('last item is', int(sortedA[-1:]))
    # print('sorted a is ', sortedA)
    
    last_index = (len(A)-1)
    length = len(A)
    print ('last one', last_index)
    for i in range(0, length, 2):
        # print('current value of i is', i)
        
        if(i >= len(A)-1):
            # print('last item is', sortedA[last_index])
            return sortedA[last_index]
            
        elif(sortedA[i] != sortedA[i+1]):
            return sortedA[i]
    