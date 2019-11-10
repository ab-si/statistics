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

X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

X_new_R = X_new-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(Y)

for i in Y_new:
    print(round(float(i),2))