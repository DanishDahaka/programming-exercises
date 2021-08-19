from fractions import Fraction

def geometric_distribution(n,p,q):

    return (q ** (n-1)) * p 



### Task 1 ###

# we are asking about the fifth produced product and have a 1/3 probability of defects
n, p  = 5, Fraction(1,3)
q =  1 - p

# rounding result to three digits
print(f'{float(geometric_distribution(n,p,q)):.3f}')


### Task 2 ###
res = 0

# to find 1 defect during the first 5 inspections means we add events 1 until including 5
for i in range(1,6):

    res += geometric_distribution(i,p,q)

print(f'{float(res):.3f}')

### alternative way to avoid loop for task 2 adapted from shabab477, calculate the complement P(X>5) ###

print(f'{1 - (1 - (1 / 3))**5:.3f}')

