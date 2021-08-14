# passes only 3 of 4 tests because probably too high complexity

def fibonacci_n_digit(digits):
    a,b = 1,1
    counter = 1
    while len(str(a))<digits:
        a,b = b,a+b
        counter += 1
    return counter

if __name__ == '__main__':

    for _ in range(int(input())):
        print(fibonacci_n_digit(int(input())))