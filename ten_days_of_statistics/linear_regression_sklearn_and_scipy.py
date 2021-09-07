### sklearn approach ###
from sklearn.linear_model import LinearRegression
import numpy as np


math, stats = np.array([95,85,80,70,60]),np.array([85,95,70,65,70])
            

# fit model for predictions
reg = LinearRegression().fit(math.reshape(-1,1), stats.reshape(-1,1))

preds = reg.predict([[80]])

prediction = list(map(lambda x :float(x),preds.round(3)))

print(f'{prediction}') # prints 78.288 inside a list