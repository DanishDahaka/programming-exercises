# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import random as r

def rotate_array(A):

    # initalise array with zeroes, maybe not necessary
    rotated_array = [0 for element in A] # -> [0,0,0,0,0]

    for index, element in enumerate(A):
        
        # case we have the last element of the array
        if index == len(A)-1: # if 4 == 4
        
            rotated_array[0] = element # rotated_array[0] = 6
        else:
            rotated_array[index+1] = element # rotated_array[1] = 3

    return rotated_array

def solution(A, K):
    # write your code in Python 3.8.10
    """ right-rotating an array A for K times 

    N/K = {[0..100]}

    Args:
    A: (array)
    K: (integer)

    returns:
    solution (array): right-rotated array
    """
    # case no rotations, forgot this one first!
    if K == 0:
        return A
    
    solution = []
    current_array = A

    #print(f'this is current_array {current_array}')
    
    for i in range(K):

        solution = rotate_array(current_array)
        # re-assign current progress to A
        current_array = solution

    

    return solution


    """
    A = [3, 8, 9, 7, 6]
    K = 3
    
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

    AND

    A = [0, 0, 0]
    K = 1

    [0, 0, 0]
    """

print(solution([-4], 0))

print(solution([r.randint(-20,20) for num in range(15)], 15))