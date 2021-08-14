import math

def fibonacci_fast(n):
    sqrt_five = math.sqrt(5)
    
    return int(((math.pow((1+sqrt_five)/2,n) - math.pow((1-sqrt_five)/2,n))/sqrt_five))

def find_golden_fib_nugget(k):
    
    return fibonacci_fast(2*k)*fibonacci_fast(2*k+1)
    
if __name__ == '__main__':    
    for _ in range(int(input())):
        number = int(input())
        print(int((find_golden_fib_nugget(number)%(math.pow(10,9)+7))))
    