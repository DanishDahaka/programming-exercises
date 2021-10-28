from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd

# retrieve input for features and rows
F, N = map(int,input().split())

# define lists to store input
X, y = [], []

# read in all rows
for rows in range(0,N):
    
    nums_in = list(map(float, input().split()))
    
    # add target variable
    y.append(nums_in[-1])
    
    # remove y element
    nums_in.pop()
    
    # add remaining elements to X
    X.append(nums_in)

preds_num = int(input())

# store number of values to predict
predictors = [list(map(float, input().split())) for j in range(preds_num)]

# transform X values into a df
X_df = pd.DataFrame(X)
    
#print(f'these are our X values as a df {X_df}')
#print(f'\nthese are our y values {y}')

# default Polynomial parameter is 2
poly_reg = PolynomialFeatures(3)


lin_reg = LinearRegression()

y = np.array(y)

lin_reg.fit(poly_reg.fit_transform(X_df),y)

"""print('Intercept: \n', lin_reg.intercept_)
print('Coefficients: \n', lin_reg.coef_)

print(f'these are our predictors {predictors}')"""

# print list of lists separated by new lines

#print(f'shape of x is {X_df.shape}')
#print(f'shape of y is {y.shape}')

print(*(lin_reg.predict(poly_reg.fit_transform(predictors))))