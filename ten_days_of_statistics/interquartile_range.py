from quartiles import quartile_calculations


def calculate_iqr(arr):

    q_one, median, q_three = quartile_calculations(arr)

    return q_three - q_one

# HackerRank adjustment
if __name__ == '__main__':

    """ n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))"""

    val = [10,40,30,50,20]

    freq = [1,2,3,4,5]

    arr = [i for l in ([a]*f for a, f in zip(val, freq)) for i in l]

    print(round(float(calculate_iqr(arr)),1)) # returns 30.0