# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.

A bounded slice is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to K.
 More precisely it is a slice, such that max(A[P], A[P + 1], ..., A[Q]) − min(A[P], A[P + 1], ..., A[Q]) ≤ K.

The goal is to calculate the number of bounded slices.

For example, consider K = 2 and array A such that:
    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3

There are exactly nine bounded slices: (0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4). -> tuples!

Thus, in this case, the function should return 9.



        N is an integer within the range [1..100,000];
        K is an integer within the range [0..1,000,000,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

"""

from itertools import combinations

def solution(K, A):
    # write your code in Python 3.8.10


    # creates {0: 3, 1: 5, 2: 7, 3: 6, 4: 3}
    idx_list = [index for index, value in enumerate(A)]

    combs_array = list(combinations(idx_list,2))


    # now combs_array should look like: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), 
    # (2, 4), (3, 4), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]


    # create index of information we want to access later in form of a hashtable
    our_hash_results = {}

    for combination in combs_array:

        our_hash_results[combination] = max(A[combination[0]:combination[1]+1])-min(A[combination[0]:combination[1]+1]) # may this be the part where O(n^3) results from?


    result_list = []

    for combination, value in our_hash_results.items():

        if value <= K:
            result_list.append(combination) # will look like [(0, 1), (1, 2), (1, 3), (2, 3)]

    # add the symmetrical pairs, e.g. (0,0), (1,1) etc. since all value == 0
    no_bounded_slices = len(result_list)+len(A)

    if no_bounded_slices > 1000000000:
        return 1000000000

    return no_bounded_slices  




print(solution(2,[3,5,7,6,3]))



