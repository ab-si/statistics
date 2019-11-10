# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

'''
The first line contains 2 space-separated integers, m (the number of observed features) and
n (the number of feature sets)

Each of the n subsequent lines contain m+1 space-separated decimals
the first m elements are features and
the last element is the value of Y for the line's feature set.

The next line contains a single integer,q , denoting the number of feature sets
for query
Each of the q subsequent lines contains m space-separated decimals describing the feature sets.
'''
import numpy as np
from sklearn import linear_model

m,n = [int(i) for i in input().strip().split(' ')]
X = []
Y = []
for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
q = int(input().strip())
X_new = []

for x in range(q):
    X_new.append(input().strip().split(' '))
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
y_pred = lm.predict(X_new)
for x in y_pred:
    print(x[0])
