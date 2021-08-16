""" adapted this function with code for sum of squares from I_Am_True"""


def calculate(n) -> int:

    natural_sum_squared = sum((i for i in range(1,n+1)))**2

    sum_of_squares = n*(n+1)*(2*n+1)//6

    return natural_sum_squared - sum_of_squares

