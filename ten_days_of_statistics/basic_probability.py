from itertools import product

### TASK 1 ###
"""In a single toss of 2 fair (evenly-weighted) six-sided dice, 
find the probability that their sum will be at most 9."""

# merge dice result tuples into summed values
dice_results = list(map(sum, product(range(1,7),repeat=2)))

over_nine = [i for i in dice_results if i <= 9]

# solution as percentage, 0.8333 == 30 / 36
print(len(over_nine)/36)

### TASK 2 ###

"""In a single toss of 2 fair (evenly-weighted) six-sided dice, 
find the probability that the values rolled by each die will be different 
and the two dice have a sum of 6."""

# get all dice results still as tuples
different_dice_results = list(product(range(1,7), repeat=2))

# check for two conditions: 1 -> die number is different and 2 -> sum is exactly 6
different_results_six_sum = [i for i in different_dice_results if i[0]!=i[1] and sum(i) == 6]

# solution as percentage, 0.111 == 1/9
print(len(different_results_six_sum)/len(different_dice_results))