import numpy as np
from sklearn.linear_model import LinearRegression

x= np.array([[1000],[2000],[3000],[4000],[5000]])
y= np.array([100,200,300,400,500])

model=LinearRegression()
model.fit(x,y)
pred = model.predict([[2500]])
print('Pred',pred)
