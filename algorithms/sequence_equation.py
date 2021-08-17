def find_element_at_index(arr, index_list) -> list:

    """returns a list of indices incremented by 1"""

    return [arr.index(i)+1 for i in index_list]



def permutation_equation(arr) -> list:

    p_two = find_element_at_index(arr, [i for i in range(1,len(arr)+1)])

    p_three = find_element_at_index(arr, p_two)

    return p_three
        
    
print(permutation_equation([5,2,1,3,4]))