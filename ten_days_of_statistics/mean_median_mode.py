from collections import Counter

def mean(array):

    amount = len(array)
    
    # divide sum of elements through number of elements
    return sum(array)/amount
    
def median(array):

    amount = len(array)
    
    s = sorted(array)

    # case even array length
    if amount % 2 == 0:

         # divide sum of the two middle elements
        return ((s[(amount//2)-1] + s[amount//2]) / 2)
    
    # case odd array length 
    else:
        # get middle value, paying attention to zero-indexed array
        return s[amount//2]
    

def mode(array):
    
    # count all values in dict
    counted = Counter(array)
    
    # store max value
    max_value = max(counted.values())
	  
    # get list of keys for the highest values in counted
    max_values = [k for k,v in counted.items() if v == max_value]
    
    return (min(max_values))

if __name__ == '__main__':
    
    amount = int(input())

    array = list(map(int, input().split()))
    
    print(mean(array), median(array), mode(array), sep = '\n')
