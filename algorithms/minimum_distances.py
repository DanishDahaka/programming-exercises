from collections import Counter
from itertools import groupby
from operator import itemgetter

def minimum_distance(arr):

    """Returns the minimum distance between
     two equal pairs of integers in a given array
     
     Args:
     arr (list):
     
     ----- 
     Returns:
     min_distance (int): the minimum distance between
     said pair of integers or -1 if there cannot be one found
     """

    # count elements in array
    count = Counter(arr)

    # create dict of pairs, filter for twice occuring elements
    dict_of_pairs = dict(filter(lambda elem: elem[1] == 2, 
                                count.items()))

    if len(dict_of_pairs) > 0:
    
        # get index and element from arr which is a pair together as tuple
        index_elements = [(index, element) for index, element in enumerate(arr) 
                        if element in dict_of_pairs.keys()]

        # sort array by second tuple element
        sorted_index_elements = sorted(index_elements, key=itemgetter(1))

        # move indices from pairs together into one tuple
        tuple_distances = [tuple(i[0] for i in e) for _, e in 
                            groupby(sorted_index_elements, lambda x: x[1])]

        # get the absolute distance between these indices
        distances = [abs(tup[0] - tup[1]) for tup in tuple_distances]

        return min(distances)

    # if there was no pair found
    else:
        return -1
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))

    print(minimum_distance(arr))