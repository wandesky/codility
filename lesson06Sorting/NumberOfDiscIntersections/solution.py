'''
I somehow gave up on this one
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    lenyA = len(A)
    # [[0,1],[0,1]]
    # minymaxy = []
    intersections = set()
    
    for currentpos in range(0, lenyA, 1):
        curr_radius = A[currentpos]
        # currentpos = i
        currentminy, currentmaxy = currentpos - curr_radius, currentpos + curr_radius
        
        for checkypos in range(currentpos+1, lenyA, 1):
            checky_radius = A[checkypos]
            checkymaxy, checkyminy = checkypos + checky_radius, checkypos - checky_radius
            if(((checkyminy <= currentminy) and (checkymaxy >= currentminy)) or ((checkyminy <= currentmaxy) and (checkymaxy >= currentmaxy)) ):
                intersections.add((currentpos, checkypos))
                
    print('intersections is ', intersections)
    return int(len(intersections))