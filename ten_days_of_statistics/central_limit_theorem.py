### Task 1 ###

# as n is large (9800), we assume a normal distribution, re-using code from normal_distribution.py
import math
from normal_distribution import cdf_normal_distribution

def mean_sum(mean, n):
    return n * mean

def sigma_sum(std, n):
    return math.sqrt(n) * std

mean, std, n, x = 205, 15, 49, 9800


print(f'{cdf_normal_distribution(mean_sum(mean, n), sigma_sum(std, n), x):.4f}')


### Task 2 ###

mean, std, n, x = 2.4, 2.0, 100, 250


print(f'{cdf_normal_distribution(mean_sum(mean, n), sigma_sum(std, n), x):.4f}')


### Task 3 ###

mean, std, n, interval, z = 500, 80, 100, 0.95, 1.96

print(f'{(mean - (std / (n ** 0.5)) * z):.2f}')
print(f'{(mean + (std / (n ** 0.5)) * z):.2f}')
