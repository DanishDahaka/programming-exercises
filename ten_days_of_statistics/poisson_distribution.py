import math

def poission_distribution(l, k, e):

    return ((l ** k) * (e ** - l) / math.factorial(k))

# eulers number
e = 2.71828


### Task 1 ###
# # https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# average is 2.5, question is to find proba of k being 5
print(f'{poission_distribution(2.5,5,e):.3f}')


### Task 2 ###

# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem


### adapted from Matthew_W_Noble's approach ###

# Input from stdin
averageX, averageY = [float(num) for num in input().split(" ")]

# alternative with using map
averageX, averageY = map(float, input().split())

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))