def unique_integer(a):
    
    # 0 cannot be at the end of the ascending sorted list
    sorted_arr = sorted(a)+[0]
    
    i = 0
    
    while True:
        
        # case both elements a pair
        if sorted_arr[i] == sorted_arr[i+1]:
            
            # move one pair forward
            i += 2
        else:
            return sorted_arr[i]
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = unique_integer(a)

    fptr.write(str(result) + '\n')

    fptr.close()