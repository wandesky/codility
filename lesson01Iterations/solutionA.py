# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    biny = bin(N)[2:]
    # print(N)
    # print(biny)
    stringy = list(str(biny))
    # print(stringy)
    max_count = 0
    temp_count = 0
    flip_occured = False
    
    for i in range(0, len(stringy), 1):
        while (i < len(stringy) and stringy[i] == '0'):
            temp_count += 1
            i += 1
        if (i < len(stringy) and stringy[i] == '1' and stringy[i-1] == '0'):
            flip_occured = True
        else:
            flip_occured = False
        if (flip_occured and temp_count > max_count):
            max_count = temp_count
        temp_count = 0
        
    return max_count