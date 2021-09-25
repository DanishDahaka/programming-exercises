def fairRations(B) -> str:

    """distribute bread loaves to people (who are represented through 
    an array with number of loaves) until all people have an even number of loaves.
    When distributing, you have to give the current person and the neighbor (i+1) person a loaf.
    
    Args: 
    B (list): people with number of loaves holding currently
    
    
    Returns:
    counter (string): number of loaves which were distributed casted to string
    or 'NO' in case the loaves cannot be distributed because there would never be only even numbers.
    """
    
    counter = 0
    amount_of_uneven = 0

    for bread_amount in B:
        
        # if the value is uneven
        if bread_amount % 2 != 0:
            
            amount_of_uneven += 1

        
    for i in range(len(B)-1):
        
        if B[i] % 2 != 0:
            
            B[i] += 1
            # add one to behind person
            B[i+1] += 1
                
            # increment counter by 2 since two people received loaves
            counter += 2
                
    return str(counter) if amount_of_uneven % 2 == 0 else 'NO'
                
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
