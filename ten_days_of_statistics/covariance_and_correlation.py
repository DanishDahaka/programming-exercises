from mean_median_mode import mean
from standard_deviation import standard_deviation

def covariance(arrx, arry) -> float:

    """Given two arrays, calculate their covariance
    
    Args:
    arrx (list): Values of X
    arry (list): Values of Y
    
    Returns:
    cov (float): covariance
    """


    # check that inserted arrays are of same length
    assert len(arrx) == len(arry)

    cov = 0

    meanx, meany = mean(arrx), mean(arry)

    # increment cov result
    for i in range(len(arrx)):

        cov += (arrx[i] - meanx) * (arry[i] - meany)

    return cov


def calculate_pcc(arrx, arry) -> float:
    
    """Given two arrays, calculate their pearson correlation coefficient
    
    Args:
    arrx (list): Values of X
    arry (list): Values of Y
    
    Returns:
    pcc (float): pearson correlation coefficient
    """


    # check that inserted arrays are of same length
    assert len(arrx) == len(arry)

    # get standard deviation for both arrays
    sdx, sdy = standard_deviation(arrx), standard_deviation(arry)

    cov = covariance(arrx, arry)
    
    pcc = cov / (len(arrx) * sdx * sdy)

    return round(pcc, 3)

def calculate_rank(vector) -> list:
    # adapted from Yuvraj Singh's version found on stackoverflow
    # https://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python

    """Given a vector, return an integer rank vector
    
    Args:
    vector (list): Values of vector
    
    Returns:
    (list): ranked values of vector
    """

    a = {}
    rank = 1

    for num in sorted(vector):

        if num not in a:

            a[num]=rank
            rank=rank+1

    return[a[i] for i in vector]


def spearman_rank_correlation(arrx, arry) -> float:

    """Given two arrays, calculate their spearman rank correlation coefficient
    
    Args:
    arrx (list): Values of X
    arry (list): Values of Y
    
    Returns:
    spearman (float): spearman rank correlation coefficient
    """

    # check for duplicates in lists
    no_duplicates = len(arrx) == len(set(arrx)) and len(arry) == len(set(arry))

    if no_duplicates:

        differences = [(x-y)**2 for x,y in zip(calculate_rank(arrx),calculate_rank(arry))]
        
        n_s = len(arrx) * ((len(arrx) ** 2) - 1)
        
        frac = 6 * sum(differences) / n_s

        spearman = 1 - frac


    else: 

        rankx, ranky = calculate_rank(arrx), calculate_rank(arry)
        #print(f'both rank lists: {rankx} and {ranky}')

        spearman = calculate_pcc(rankx, ranky)


    return spearman




# Hackerrank code moved to main method
if __name__ == '__main__':


    # from AI challenge about pearson corr coeff
    # https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
    xi_s = [15,12,8,8,7,7,7,6,5,3]
    yi_s = [10, 25, 17, 11,  13,  17,  20,  13,  9,  15]

    print(calculate_pcc(xi_s, yi_s))