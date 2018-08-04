'''
This one works 
(Remember, a negative number multiplied by another negative number returns a positive number)
'''
def solution(A):
    #sort the contents of A
    #find maxy1 by multiplying last three elements of sortedA
    #find maxy2 by multiplying first two elements of sortedA with the last element of sortedA
    #return larger one between maxy1 and maxy2

    sorty = sorted(A)
    leny = len(sorty)
    maxy1 = sorty[leny - 1] * sorty[leny - 2] * sorty[leny - 3]
    maxy2 = sorty[0] * sorty[1] * sorty[leny - 1]

    maxy = max(maxy1, maxy2)

    return maxy
    