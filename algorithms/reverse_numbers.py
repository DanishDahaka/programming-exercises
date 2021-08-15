def reverse_divisable(number, divisor) -> bool:
    
    string_format = str(number)
    
    reversed_number = int(string_format[::-1])
    
    if (number - reversed_number) % divisor == 0:
        
        return True
    
    return False
    

def beautifulDays(i, j, k) -> int:
            
    return len([1 for num in range(i,j+1) if reverse_divisable(num, k)])


if __name__ == '__main__':

    print(beautifulDays(20,23,6))