# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    lenyA = len(A)
    # [[0,1],[0,1]]
    # minymaxy = []
    intersections = set()
    
    for currentpos in range(0, lenyA, 1):
        print('currentpos is ', currentpos)
        curr_radius = A[currentpos]
        # currentpos = i
        currentminy, currentmaxy = currentpos - curr_radius, currentpos + curr_radius
        
        for checkypos in range(0, lenyA, 1):
            if(currentpos == checkypos):
                    checkypos += 1
            if(checkypos < lenyA):
                checky_radius = A[checkypos]
                checkymaxy, checkyminy = checkypos + checky_radius, checkypos - checky_radius
                if(((checkyminy <= currentminy) and (checkymaxy >= currentminy)) or ((checkyminy <= currentmaxy) and (checkymaxy >= currentmaxy)) ):
                    print('success ', currentpos, checkypos)
                    
                    intersections.add( (min(currentpos, checkypos), max(currentpos, checkypos)) )
                    print('inter update ', intersections)
                    
    print('intersections is ', intersections)
    return int(len(intersections))