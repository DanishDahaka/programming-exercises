from mean_median_mode import mean
import math

def standard_deviation(arr):

    mean_value = mean(arr)

    mean_subtracted = [i - mean_value for i in arr]

    squared = [i ** 2 for i in mean_subtracted]

    return math.sqrt(sum(squared)/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(round(standard_deviation(vals)),1)