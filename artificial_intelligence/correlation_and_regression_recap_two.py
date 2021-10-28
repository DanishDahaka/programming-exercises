import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([15,12,8,8,7,7,7,6,5,3], float)
y = np.array([10,25,17,11,13,17,20,13,9,15],float)

linreg = LinearRegression()

linreg.fit(X.reshape(-1, 1),y)

print(np.round(linreg.coef_,3))