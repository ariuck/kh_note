#지도학습
#R2
#MAE
#MSE(root)
#선형회귀
#과소적합
#과적합

import numpy as np
from numpy.ma.core import reshape
from sklearn.linear_model import LinearRegression

# y = 3x + 2
X = np.linspace(1, 100, 10)
y = X * 3 +2
X =  X.reshape(-1,1)

m = LinearRegression()
m.fit(X,y)

print("m.coef_ : " , m.coef_)
print("m.intercept_ : " , m.intercept_)