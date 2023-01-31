"""For example, given N = 1041 the function should return 5, 
because N has binary representation 10000010001 and so its longest binary gap is of length 5. 
Given N = 32 the function should return 0, because N has binary representation '100000' 
and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647]."""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def rec_decimal_to_binary(number):

    """trys to cast given input to int and returns binary representation
    
    Arguments:
    number          (int): an integer to be converted


    Returns:
    binary_int      (int): the binary representation of the integer
    """

    num = int(number)

    if num >= 1:
        rec_decimal_to_binary(num//2)

    print(num%2, end='')


    # 4 = 10, 2 = 1, 1 = 0; 1000 = 111

    """important realisation: 
    When trying to estimate the binary representation of a number,
    one can assume that the multiplier of the current number resulting in the solution
    would be the remaining exponent required to add to the current exponent.
    
    Example: We want to know what x is in 512 = 2^x. 
    We start going through the 2^x series.
    8 is 2^3.
    64 is 2^6. 64 is 8 times in 512.
    So there might be a chance to find 512 by adding the exponents of 2^6 (64) and 2^3 (8).
    And indeed, 512 is 2^(6+3) or 2^9.
    
    How would this work for 4096?
    We have this number 8 times in 512, hence it could be 2^(9+3).
    2^10 = 1024, 2^11 = 2048, 2^12 = 4096. Hmm, this does seem to work for the next int.
    
    
    Now how about finding 2^20 based on this?
    2^10 = 1024 -> either multiplying 1024 with 1024, OR 2^5 four times (32*32*32*32).
    1000 * 1024 -> 1024000
    24 * 1000   ->   24000
    24 *   20   ->     480
    24 *    4   ->      96

    result would be 1048576.  
    """


def solution(N):
    # write your code in Python 3.8.10
    binary_list = bin(N)[2:]

    results = []
    curr = 0
    got_one = False

    for char in binary_list:
        if char == '1' and got_one == False:
            got_one = True
        elif char == '0' and got_one == True:
            curr += 1
        elif char == '1' and got_one == True:
            results.append(curr)
            curr = 0
        else:
            continue

    return 0 if len(results)==0 else max(results)


print(solution(32)) # should return 0
print(solution(529)) # should return 4