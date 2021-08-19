### Binomial Distribution Task I ###

# taken from brianmvance's approach:

import math

def bi_dist(x, n, p):

    b = (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * (p**x) * ((1-p) ** (n-x))

    return(b)

b, p, n = 0, 1.09/2.09, 6

# calculate for at least 3 boys
for i in range(3,7):

    b += bi_dist(i, n, p) 

# rounding to three digits
print("%.3f" %b)

### Task II, re-using formula from above ###
one,two = 0,0

# 1. no more than 2 rejects
for reject in range(0,3):

    one += bi_dist(reject, 10, 0.12)

print("%.3f" %one)

# 2. at least 2 rejects, e.g. 2 until including 10
for reject in range(2,11):

    two += bi_dist(reject, 10, 0.12)

print("%.3f" %two)