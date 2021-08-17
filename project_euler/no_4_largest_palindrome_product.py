from itertools import combinations

### solution is not efficient enough for HackerRank compiler to finish all four test cases ###

n = 1000000

three_digit_values = [i for i in range(100,1000)]

all_combinations = list(combinations(three_digit_values, 2))

products = [x*y for (x,y) in all_combinations if x*y <= n]

# only keep products if they are palindromes, e.g. same beginning and ending
palindrome_products = [i for i in products if str(i) == str(i)[::-1]]

# get tuples of index and distance from the required number
distances = [(ind, abs(i - n)) for ind, i in enumerate(palindrome_products)]


print(palindrome_products[min(distances, key = lambda t: t[1])[0]]) # evaluates to 906609