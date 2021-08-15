#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    
    weighted_arr = [elem*weight for elem,weight in zip(X,W)]
    
    return sum(weighted_arr)/sum(W)
    

if __name__ == '__main__':
    
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    # round result for exercise to 1 digit
    print(round(weightedMean(vals, weights),1))
