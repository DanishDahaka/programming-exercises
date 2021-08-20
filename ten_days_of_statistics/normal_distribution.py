import math

# adapted after code from augustocmen

mean, std = 20, 2

def cdf_normal_distribution(mean, std, x):

    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print(f'{cdf_normal_distribution(mean, std, 19.5):.3f}')
# Between 20 and 22
print(f'{cdf_normal_distribution(mean, std, 22) - cdf_normal_distribution(mean, std, 20):.3f}')

### Task 2 ###

# beware, wished output is different, e.g. percentage 10.25

def cdf_normal_distribution_percentage(mean, std, x):

    return (0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))) * 100

### Task 2 ###

mean, std = 70, 10

# higher than 80
print(f'{100-cdf_normal_distribution_percentage(mean, std, 80):.2f}')

# equal or larger 60
print(f'{100-cdf_normal_distribution_percentage(mean, std, 60):.2f}')

# less than 60
print(f'{cdf_normal_distribution_percentage(mean, std, 60):.2f}')
