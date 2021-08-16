def advertise(n):

    total = 0
    friends = 3
    likes = 0
    receive = 5
    
    for _ in range(1,n+1):
            
        likes = receive // 2

        receive = likes * friends
        
        total += likes
    
    return total
