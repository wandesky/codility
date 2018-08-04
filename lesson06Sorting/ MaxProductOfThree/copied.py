# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    
    A = sorted(A)

    product_A = A[0] * A[1] * A[-1]
    product_B = A[-1] * A[-2] * A[-3]
    max_product = max(product_A, product_B)

    return max_product