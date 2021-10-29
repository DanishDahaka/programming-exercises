from sklearn.linear_model import LinearRegression
import numpy as np

in_string = """Physics Scores  15  12  8   8   7   7   7   6   5   3 \n
History Scores  10  25  17  11  13  17  20  13  9   15"""

#print(in_string.split('\n')[2].split())

X = np.array(list(map(float,in_string.split('\n')[0].split()[2:])))
y = np.array(list(map(float,in_string.split('\n')[2].split()[2:])))

#print(f'types of X is:{type(X)} and y: {type(y)}')
#print(f'content of X: {X} \n and y:{y}')

linreg = LinearRegression()

linreg.fit(X.reshape(-1,1),y)

print(*linreg.predict(np.array(10).reshape(1,-1)))