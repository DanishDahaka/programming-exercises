from mean_median_mode import median

def quartile_calculations(arr):

    """ Prepare dataset for quartiles through sorting and slicing.
    
    Arguments:
    arr (list): array of numbers 

    Returns:
    tuple of three, consisting of:

    first_half (int): the first part of the ordered dataset up until median value
    second_half (int): the second part of the ordered dataset from the median value
    median_value (int): the middle value of the ordered dataset
    """

    # sort ascending inplace
    arr.sort()

    median_value = median(arr)

    array_length = len(arr)
    

    # case array length is even
    if array_length % 2 == 0:

        middle = array_length//2
        
        # split dataset exactly in half
        first_half, second_half = arr[:middle], arr[middle:]

    # case odd array length
    else:
        
        # integer division to get index from median
        middle = array_length//2

        # exclude median from splits
        first_half, second_half = arr[:middle], arr[middle+1:]

    return (median(first_half), median_value, median(second_half))

    """return statement for HackerRank as integer list instead:"""
    #return [int(median(first_half)), int(median_value), int(median(second_half))]

if __name__ == '__main__':
    # example test case
    arr = [9,5,7,1,3]

    first_quartile, median_value, second_quartile = quartile_calculations(arr)

    # casting for integer case
    print(int(first_quartile), int(median_value), int(second_quartile), sep = '\n')
